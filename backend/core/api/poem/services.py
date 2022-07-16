from db.models import Poem


class RetrievePoem:
    def __init__(self, params):
        self.params = params.query_params

    def run(self):
        return Poem.objects.filter(**self.params)
