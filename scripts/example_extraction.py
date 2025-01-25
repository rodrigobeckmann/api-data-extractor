from api_extractor.extractors.example_api import ExampleApiClient
from api_extractor.file_manager import FileManager

def run_extraction():
    client = ExampleApiClient()
    file_manager = FileManager()    
    result = client.get_data(params=dict(
        drilldowns="Nation",
        measures="Population",
    ))

    data = result["data"]

    file_manager.save_json(data, file_name="example_data")
    file_manager.save_csv(data, file_name="example_data")

run_extraction()
