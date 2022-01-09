from types import SimpleNamespace
import pygame
from pygame import *
from pygame import gfxdraw


def initializeView(graph_info):
    WIDTH, HEIGHT = 1080, 720
    pygame.init()

    screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
    clock = pygame.time.Clock()
    pygame.font.init()

    # load the json string into SimpleNamespace Object

    for n in graph_info.Nodes:
        x, y, _ = n.pos.split(',')
        n.pos = SimpleNamespace(x=float(x), y=float(y))

    # get data proportions
    min_x = min(list(graph_info.Nodes), key=lambda n: n.pos.x).pos.x
    min_y = min(list(graph_info.Nodes), key=lambda n: n.pos.y).pos.y
    max_x = max(list(graph_info.Nodes), key=lambda n: n.pos.x).pos.x
    max_y = max(list(graph_info.Nodes), key=lambda n: n.pos.y).pos.y

    def scale(data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    # decorate scale with the correct values

    def my_scale(data, x=False, y=False):
        if x:
            return scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, screen.get_height() - 50, min_y, max_y)

    return my_scale, screen, clock


def display_update(agents, pokemons, graph_info, my_scale, screen, clock, info, ttl):
    FONT = pygame.font.SysFont('Arial', 20, bold=True)
    font = pygame.font.SysFont('Arial', 18)
    # agents:
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))

    # pokemons:
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
    for n in graph_info.Nodes:
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
    for e in graph_info.Edges:
        # find the edge nodes
        src = next(n for n in graph_info.Nodes if n.id == e.src)
        dest = next(n for n in graph_info.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(112, 223, 145), (int(agent.pos.x), int(agent.pos.y)), 10)

    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked
    # in the same way).
    for p in pokemons:
        if p.type > 0:
            pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
        else:
            pygame.draw.circle(screen, Color(255, 0, 0), (int(p.pos.x), int(p.pos.y)), 10)

    # Timer window
    pygame.draw.rect(screen, (176, 224, 230), [20, 17, 100, 45], border_radius=15)
    font = pygame.font.SysFont('Arial', 18)
    time_text = font.render("Timer: " + str(ttl), True, Color(0, 0, 0))
    screen.blit(time_text, (33, 30))

    # Moves counter window
    moves = info['GameServer']['moves']
    pygame.draw.rect(screen, (176, 224, 230), [136, 17, 95, 45], border_radius=15)
    moves_text = font.render("Moves: " + str(moves), True, Color(0, 0, 0))
    screen.blit(moves_text, (146, 30))

    # Stop button
    button = pygame.Rect(245, 17, 80, 45)
    stop_text = font.render("Stop", True, Color(255, 255, 255))
    pygame.draw.rect(screen, (245, 10, 10), button, border_radius=15)
    screen.blit(stop_text, (268, 30))

    # Update screen
    display.update()
    clock.tick(60)
    return agents, pokemons, button
