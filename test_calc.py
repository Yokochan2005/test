# 1.ファイル名は「test_対象のモジュール名.py」とする
# 2. unittestモジュールをimportする
import unittest
import calc

# 3.テストクラス名は「Testテスト対象のクラス名」とする
# 4.テストクラスはunittest.TestCaseを継承する
class TestCalc(unittest.TestCase):

    # 5.テストメソッド名は「test_テスト対象のメソッド名」とする
    def test_add_num(self):
        num1 = 10
        num2 = 5
        expected = 15
        actual = calc.add_num(num1, num2)

        # 予定の結果を得られているか確認するassertEqual()メソッド
        self.assertEqual(expected, actual)

    def test_sub_num(self):
        num1 = 10
        num2 = 5
        expected = 5
        actual = calc.sub_num(num1, num2)
        self.assertEqual(expected, actual)

# 6. unittest.main()でテストを実行する
if __name__ == "__main__":
    unittest.main()
