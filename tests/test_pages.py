

def test_homepage(client, app):
    # test that viewing the page renders without template errors
    # assert client.get("/auth/register").status_code == 200
    """
        Home Page tests
        Ensures that the nav-tem for 'reports' endpoint exits in the rendered html
    """

    with app.app_context():
        r = client.get("/")

        assert r.status_code == 200

        # Test Nav Item
        assert "Reports" in r.get_data(as_text=True)


def test_reports_list(client, app):
    """
        Reports List Page tests
        Ensures that the page gets the appropriate redirect to the get all reports
        Also ensures that 404 page is returned if not found resource
    """
    with app.app_context():
        r = client.get("/reports")

        assert r.status_code == 308

        r = client.get("/repo")
        assert r.status_code == 404
        assert "Sorry" in r.get_data(as_text=True)


def test_report_resource(client, app):
    """
        Individual Report Page tests
        Ensures that the appropriate resource gets retrieved and rendered on the individual page of each report
        Also ensures that 404 page is returned if not found resource
    """
    with app.app_context():
        r = client.get("/reports/1")
        assert r.status_code == 200
        assert "Organization: Dunder Mifflin" in r.get_data(as_text=True)

        # Test Invalid reports
        r = client.get("/reports/111")
        assert r.status_code == 404


