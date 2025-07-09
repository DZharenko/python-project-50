from pathlib import Path

from gendiff.gendiff_engine.generate_diff import generate_diff


def get_test_file_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def test_json():
    file1_json = get_test_file_path('file1.json')
    file2_json = get_test_file_path('file2.json')
    expected_compare_2_json_files = \
        get_test_file_path('result_flat_json.txt').read_text()
    result = generate_diff(file1_json, file2_json)

    assert result == expected_compare_2_json_files
