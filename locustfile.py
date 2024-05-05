from locust import HttpUser, task, between

class WebsiteUser(HttpUser):

    wait_time = between(1, 5)
    @task()
    def view_homepage(self):
        self.client.get("/")
    @task(3)
    def view_posts(self):
        self.client.get("/posty")

    @task(3)
    def view_albums(self):
        self.client.get("/albumy")

    @task()
    def view_post(self):
        self.client.get("/posty/1")

    @task()
    def view_album(self):
        self.client.get("/albumy/1")

    @task()
    def view_limit(self):
        self.client.get("/limit")

    @task()
    def view_filtr(self):
        self.client.get("/filtr")

# /
# /posty
# /albumy
# /posty/post_id
# /albumy/album_id
# /limit
# /filtr


# Ustawienie czasu oczekiwania między zadaniami na 1 do 5 sekund.
# Pozwala to symulować rzeczywiste zachowanie użytkownika, który nie wykonuje żądań ciągle jeden po drugim,
# ale z pewnymi przerwami.

# Wykonanie żądania GET do strony bloga.
# Zadanie to jest wykonywane trzy razy częściej niż inne zadania, co oznacza,
# że symuluje większe zainteresowanie sekcją bloga przez użytkowników.


# Wykonanie żądania GET do strony głównej serwisu.
# To zadanie symuluje wejście użytkownika na stronę główną.