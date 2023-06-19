from cassandra.cqlengine.management import sync_table

class modelProcessor():
    model = ""
    def __init__(self, model):
        self.model = model

    @staticmethod
    def constructTable(self):
        sync_table(self.model)
        print("successfully loaded model")
    
    @staticmethod
    def writeModel(self, *args):
       return None

    @staticmethod
    def readModel(self, *args):
        return None
