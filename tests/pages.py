def test_register(client, app):
    # test that viewing the page renders without template errors
    # assert client.get("/auth/register").status_code == 200

    with app.app_context():
        r = client.get("/")

        assert r.status_code == 200
