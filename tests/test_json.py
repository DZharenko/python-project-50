from gendiff import generate_diff
from gendiff.parse_file import get_test_file_path


def test_json():
    file1_json = get_test_file_path('file1.json')
    file2_json = get_test_file_path('file2.json')
    expected_compare_2_json_files = \
        get_test_file_path('result_flat_json.txt').read_text()
    result = generate_diff(file1_json, file2_json)

    assert result == expected_compare_2_json_files
