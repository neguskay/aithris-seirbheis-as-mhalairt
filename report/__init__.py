from flask import Flask, render_template, request, Blueprint, redirect, url_for, make_response
# from flask.ext.sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler
from forms import *
import json
import logging
import pdfkit

from models import Local_Reports, session

report = Blueprint("reports", __name__)


@report.route("/", methods=["GET"])
def reports_list():
    reports_db_list = session.query(Local_Reports).all()

    return render_template("pages/reports.html", reports_db_list=reports_db_list)


@report.route("/<report_id>", methods=["GET"])
def report_details(report_id):
    report_dict = {
        "name": "Report One",
        "id": report_id,
        "description": "Report one is the report for the financial year one to one."
    }
    return render_template("pages/report.html", report=report_dict)


@report.route("/generate", methods=["GET"])
def generate():
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


