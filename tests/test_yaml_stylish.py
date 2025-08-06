from gendiff import generate_diff
from gendiff.gendiff_engine.parse_file import get_test_file_path


def test_json():
    file3_yaml = get_test_file_path('file3.yaml')
    file4_yaml = get_test_file_path('file4.yaml')
    expected_compare_2_json_files = \
        get_test_file_path('result_stylish_yaml.txt').read_text()
    result = generate_diff(file3_yaml, file4_yaml)

    assert result == expected_compare_2_json_files