from gendiff import generate_diff
from gendiff.gendiff_engine.parse_file import get_test_file_path


def test_yaml():
    file1_yaml_path = get_test_file_path('file1.yaml')
    file2_yaml_path = get_test_file_path('file2.yaml')
    expected_compare_2_yaml_files = \
        get_test_file_path('result_flat_yaml.txt').read_text()
    result = generate_diff(file1_yaml_path, file2_yaml_path)

    assert result == expected_compare_2_yaml_files