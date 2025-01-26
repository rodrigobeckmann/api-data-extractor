from api_extractor.extractors.example_api import ExampleApiClient
from api_extractor.file_manager import FileManager


def run_extraction():
    client = ExampleApiClient()
    result = client.get_data(
        params=dict(
            drilldowns="Nation",
            measures="Population",
        )
    )

    data = result["data"]

    FileManager.save_json(data, file_name="example_data")
    FileManager.save_csv(data, file_name="example_data")

run_extraction()
