from gendiff import generate_diff
from gendiff.gendiff_engine.parse_file import get_test_file_path


def test_json():
    file3_json = get_test_file_path('file3.json')
    file4_json = get_test_file_path('file4.json')
    expected_compare_2_json_files = \
        get_test_file_path('result_stylish_json.txt').read_text()
    result = generate_diff(file3_json, file4_json)

    assert result == expected_compare_2_json_files