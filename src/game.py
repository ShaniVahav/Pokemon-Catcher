import json
from types import SimpleNamespace
from pygame import *
import pygame
from pygame.color import Color
from pygame import gfxdraw


def display_update(client, FONT, graph, my_scale, screen, clock):
    # agents:
    agents = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))

    # pokemons:
    pokemons = json.loads(client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(pygame.Color(0, 0, 0))

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y), 15, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y), 15, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23), (int(agent.pos.x), int(agent.pos.y)), 10)
        """""
        need to change!:
        """
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked
    # in the same way).
    for p in pokemons:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)

    font = pygame.font.SysFont('Arial', 18)

    # Timer window
    pygame.draw.rect(screen, (176, 224, 230), [20, 17, 80, 45], border_radius=15)
    time_text = font.render("Time: " + str(int(pygame.time.get_ticks() / 1000)), True, Color(0, 0, 0))
    screen.blit(time_text, (33, 30))

    # Moves counter window
    info = json.loads(client.get_info())
    moves = info['GameServer']['moves']
    pygame.draw.rect(screen, (176, 224, 230), [120, 17, 95, 45], border_radius=15)
    moves_text = font.render("Moves: " + str(moves), True, Color(0, 0, 0))
    screen.blit(moves_text, (130, 30))

    # Stop button
    button = pygame.Rect(240, 17, 80, 45)
    stop_text = font.render("Stop", True, Color(255, 255, 255))
    pygame.draw.rect(screen, (245, 10, 10), button, border_radius=15)
    screen.blit(stop_text, (263, 30))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and button.collidepoint(event.pos):
            client.stop()

    # Update screen changes and number of moves
    # moves += 1

    display.update()
    clock.tick(60)
    return agents, pokemons


"""""
def findPokemon(self, pos, type):
    for src in self.graph.nodes.keys():
        srcNode = self.graphAlgo.get_graph().nodes[src]
        for dest in self.graphAlgo.get_graph().edgesOut[src].keys():
            destNode = self.graphAlgo.get_graph().nodes[dest]
            if ((type > 0 and src < dest) or (type < 0 and src > dest)):
              #  line1 = PokemonAlgo.distance(srcNode.pos, destNode.pos)
               # line2 = PokemonAlgo.distance(srcNode.pos, pos) + PokemonAlgo.distance(pos, destNode.pos)
                #if (line1 > line2 - 0.0000001):
                    return [src, dest]
   # return null
"""


def start(client, FONT, graph, my_scale, screen, clock):
    client.start()
    while client.is_running() == 'true':
        update = display_update(client, FONT, graph, my_scale, screen, clock)
        agents = update[0]
        pokemons = update[1]

        # for p in pokemons:
        # findPokemon(p, edges)
        # choose next edge
        for agent in agents:
            if agent.dest == -1:
                next_node = (agent.src - 1) % len(graph.Nodes)
                client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
                ttl = client.time_to_end()
                print(ttl, client.get_info())

        client.move()

    # game over: