import unittest
from hypothesis import given, strategies as st
from modline import gen_modline


class TestGeneratedModline(unittest.TestCase):

    @given(lista=st.lists(st.text()), folder_name=st.text())
    def test_gen_modline(self, lista, folder_name):
        self.assertTrue(isinstance(gen_modline(lista=lista,
                                      mod_folder_name=folder_name), str))

if __name__ == '__main__':
    unittest.main()
