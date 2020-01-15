
def test_homepage(client, app):
    # test that viewing the page renders without template errors
    # assert client.get("/auth/register").status_code == 200

    with app.app_context():
        r = client.get("/")

        assert r.status_code == 200

        # Test Nav Item
        assert "Reports" in r.get_data(as_text=True)


def test_reports_list(client, app):
    with app.app_context():
        r = client.get("/reports")

        assert r.status_code == 308

        r = client.get("/repo")
        assert r.status_code == 404


def test_report_resource(client, app):
    with app.app_context():
        r = client.get("/reports/1")
        assert r.status_code == 200
        assert "Organization: Dunder Mifflin" in r.get_data(as_text=True)

        # Test Invalid reports
        r = client.get("/reports/111")
        assert r.status_code == 404


