import json
import unittest
import Algo


class TestAlgo(unittest.TestCase):

    def read_file_data(sel, filename):
        with open(filename, encoding="utf8") as data_file:
            json_data = json.load(data_file)
        return json_data

    def A(self, i):
        dict = self.read_file_data('../dataForTest/A' + str(i) + '.json')
        return Algo.Graph(dict['Nodes'], dict['Edges'])

    def test_findPokemon_A0(self):
        graphGame = self.A(0)

        e = Algo.Graph.findPokemon(graphGame, '35.199963710098416, 32.105723673136964, 0.0', 1)
        self.assertEqual(('3', 4), e)

        e = Algo.Graph.findPokemon(graphGame, '35.195224052340706, 32.10575624080796, 0.0', 1)
        self.assertEqual(('2', 3), e)

        e = Algo.Graph.findPokemon(graphGame, '35.197656770719604, 32.10191878639921, 0.0', 1)
        self.assertEqual(('8', 9), e)

    def test_findPokemon_A1(self):
        graphGame = self.A(1)

        e = Algo.Graph.findPokemon(graphGame, '35.198546018801096, 32.10442041371198, 0.0', 1)
        self.assertEqual(None, e)

        e = Algo.Graph.findPokemon(graphGame, '35.20418622066997, 32.10618391544376, 0.0', -1)
        self.assertEqual(('8', 7), e)

        e = Algo.Graph.findPokemon(graphGame, '35.207511563168026, 32.10516145234799, 0.0', -1)
        self.assertEqual(('7', 6), e)


    def test_findPokemon_A2(self):
        graphGame = self.A(2)

        e = Algo.Graph.findPokemon(graphGame, '35.198546018801096, 32.10442041371198, 0.0', 1)
        self.assertEqual(('9', 23), e)

        e = Algo.Graph.findPokemon(graphGame, '35.20418622066997, 32.10618391544376, 0.0', 1)
        self.assertEqual(('7', 8), e)

        e = Algo.Graph.findPokemon(graphGame, '35.207511563168026, 32.10516145234799, 0.0', 1)
        self.assertEqual(('6', 7), e)

    def test_findPokemon_A3(self):
        graphGame = self.A(3)

        e = Algo.Graph.findPokemon(graphGame, '35.198546018801096, 32.10442041371198, 0.0', 1)
        self.assertEqual(None, e)

        e = Algo.Graph.findPokemon(graphGame, '35.20418622066997, 32.10618391544376, 0.0', -1)
        self.assertEqual(('8', 7), e)

        e = Algo.Graph.findPokemon(graphGame, '35.207511563168026, 32.10516145234799, 0.0', 1)
        self.assertEqual(('8', 9), e)


    def test_shortestPath_A0(self):
        graphGame = self.A(0)

        path = graphGame.shortestPath(8, (0, 1))
        self.assertEqual([8, 9, 10, 0, 1], path)

        path = graphGame.shortestPath(0, (8, 9))
        self.assertEqual([0, 10, 9, 8, 9], path)

        path = graphGame.shortestPath(7, (7, 6))
        self.assertEqual([6], path)

    def test_shortestPath_A1(self):
        graphGame = self.A(1)

        path = graphGame.shortestPath(8, (0, 1))
        self.assertEqual([8, 7, 6, 2, 1, 0, 1], path)

        path = graphGame.shortestPath(0, (12, 13))
        self.assertEqual([0, 16, 15, 14, 13, 12, 13], path)

        path = graphGame.shortestPath(16, (7, 6))
        self.assertEqual([16, 0, 1, 2, 6, 7, 6], path)


    def test_shortestPath_A2(self):
        graphGame = self.A(2)

        path = graphGame.shortestPath(8, (0, 1))
        self.assertEqual([8, 26, 1, 0, 1], path)

        path = graphGame.shortestPath(0, (12, 13))
        self.assertEqual([0, 16, 15, 14, 13, 12, 13], path)

        path = graphGame.shortestPath(24, (7, 6))
        self.assertEqual([24, 25, 8, 7, 6], path)


    def test_shortestPath_A3(self):
        graphGame = self.A(3)

        path = graphGame.shortestPath(8, (0, 3))
        self.assertEqual([8, 7, 6, 5, 25, 24, 23, 22, 0, 3], path)

        path = graphGame.shortestPath(22, (15, 19))
        self.assertEqual([22, 21, 20, 19, 16, 15, 19], path)

        path = graphGame.shortestPath(24, (7, 6))
        self.assertEqual([24, 25, 5, 6, 7, 6], path)



if __name__ == '__main__':
    unittest.main()
