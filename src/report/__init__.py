from flask import render_template, request, Blueprint, redirect, url_for, make_response, abort
import pdfkit

from src.models import Local_Reports, session

report = Blueprint("reports", __name__)


@report.route("/", methods=["GET"])
def reports_list():
    """
        Route: Retrieves all report details on a page.
    """
    reports_db_list = session.query(Local_Reports).all()

    return render_template("pages/reports.html", reports_db_list=reports_db_list)


@report.route("/<report_id>", methods=["GET"])
def report_details(report_id):
    """
        Route: Retrieves individual report details on a page.
        :arg report_id PK id if the report.
    """
    report_data = session.query(Local_Reports).filter_by(id=report_id).first()

    if report_data is not None:
        return render_template("pages/report.html", report=report_data)

    else:
        abort(404)


@report.route("/generate", methods=["GET"])
def generate():
    """
       Route: Generates PDF or XML of a report upon receipt of request.
       :arg report_id PK id if the report.
       :arg output_type str pdf or xml.
    """
    response = None
    rendered_certificate = None

    report_id = request.args.get("report_id")
    output_type = request.args.get("output_type")

    if report_id is not None and output_type is not None:
        report_id = int(report_id)
        report_data = session.query(Local_Reports).filter_by(id=report_id).first()
        if report_data.get_cleaned_data() is not None:

            rendered_certificate = render_template(
                "layouts/report_pdf.html",
                report_data=report_data,
            )

            if rendered_certificate:
                # Set to False, do not send to client.
                pdf_certificate = pdfkit.from_string(
                    input=rendered_certificate, output_path=False
                )

                # make response
                response = make_response(pdf_certificate)
                file_name = f'report-{report_data.organization}-{report_data.report_date}.pdf'

                response.headers["Content-Type"] = "application/pdf"
                response.headers[
                    "Content-Disposition"
                ] = f"attachment; filename={file_name}"

    if not response:
        return redirect(url_for("reports.reports_list"))
    else:
        return response


