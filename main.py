import pygame
import random


class Platform:
    def __init__(self, sc):
        self.sc = sc
        self.main_block = pygame.image.load('data/mainblock.png')  # загрузка платформы
        self.rect = self.main_block.get_rect()
        self.sc_rect = self.sc.get_rect()
        self.rect.centerx = self.sc_rect.centerx
        self.rect.centery = 480

    def draw(self):
        self.sc.blit(self.main_block, self.rect)  # рисование платформы

    def move(self, x2):
        self.rect.centerx = x2

    def left(self):  # движение платформы влево
        if self.rect.x - 5 > 0:
            self.rect.x -= 5

    def right(self):  # движение платформы вправо
        if self.rect.x + 85 < 495:
            self.rect.x += 5


class Ball:
    def __init__(self, sc):
        self.sc = sc
        self.main_block = pygame.image.load('data/ball.png')  # загрузка картинки мяча
        self.rect = self.main_block.get_rect()
        self.sc_rect = self.sc.get_rect()
        self.rect.centerx = self.sc_rect.centerx
        self.rect.centery = 465
        self.x = '-'
        self.y = '-'

    def draw(self):
        self.sc.blit(self.main_block, self.rect)  # рисование мяча

    def move(self, p):
        x1, y1 = self.rect.x, self.rect.y
        c1 = block.x_ret()  # x координата блока
        c2 = block.y_ret()  # y координата блока
        c = block.ret()
        ind = 0
        for j in c2:  # проверка столкновения мячя с блоками
            for i in c1:
                if (i, j) not in c:
                    if i + 75 <= x1 <= i + 77:
                        if (j < y1 < j + 17) or (j < y1 + 20 < j + 17):
                            self.x = '+'
                            block.change(ind)
                    if i <= x1 + 20 <= i + 2:
                        if (j < y1 < j + 17) or (j < y1 + 20 < j + 17):
                            self.x = '-'
                            block.change(ind)
                    if j + 15 <= y1 <= j + 17:
                        if (i < x1 < i + 77) or (i < x1 + 20 < i + 77):
                            self.y = '+'
                            block.change(ind)
                    if j <= y1 + 20 <= j + 2:
                        if (i < x1 < i + 77) or (i < x1 + 20 < i + 77):
                            self.y = '-'
                            block.change(ind)
                ind += 1
        fps = 60
        if len(c) >= 15:
            fps += 10
        if x1 <= 0:  # смена направления мяча
            self.x = '+'
        if y1 <= 0:
            self.y = '+'
        if (x1 + 20) >= 495:
            self.x = '-'
        if 455 <= y1 <= 465 and p <= x1 <= p + 80:
            self.y = '-'
        if self.x == '+':  # движение мяча
            x1 += 5
        if self.x == '-':
            x1 -= 5
        if self.y == '+':
            y1 += 5
        if self.y == '-':
            y1 -= 5
        self.rect.x = x1
        self.rect.y = y1
        clock.tick(fps)

    def check(self):
        if self.rect.y >= 495:   # проверка падения шарика на землю
            life.change_level()
            return False
        return True


class Blocks:
    def __init__(self, sc):
        self.image_r = pygame.image.load('data/block_r.png')  # красный блок - 3
        self.image_g = pygame.image.load('data/block_g.png')  # зелёный блок - 1
        self.image_y = pygame.image.load('data/block_y.png')  # жёлтый блок - 2
        self.rect_r = self.image_r.get_rect()
        self.rect_g = self.image_g.get_rect()
        self.rect_y = self.image_y.get_rect()
        self.blocks = [1] * 30
        self.was = []
        self.xs = []
        self.ys = []
        self.sc = sc
        y_coor = 60
        x_coor = 10
        for _ in range(5):  # создание y-координат
            self.ys.append(y_coor)
            y_coor += 45
        for _ in range(6):  # создание х-координат
            self.xs.append(x_coor)
            x_coor += 80

    def ret(self):
        return self.was

    def draw(self):  # рисование блоков
        index = 0
        for i1 in self.ys:
            for j in self.xs:
                x_coor, y_coor = j, i1
                if self.blocks[index] == 1:
                    self.rect_g.x = x_coor
                    self.rect_g.y = y_coor
                    self.sc.blit(self.image_g, self.rect_g)
                elif self.blocks[index] == 2:
                    self.rect_y.x = x_coor
                    self.rect_y.y = y_coor
                    self.sc.blit(self.image_y, self.rect_y)
                elif self.blocks[index] == 3:
                    self.rect_r.x = x_coor
                    self.rect_r.y = y_coor
                    self.sc.blit(self.image_r, self.rect_r)
                elif self.blocks[index] == 0:
                    if (x_coor, y_coor) not in self.was:
                        self.was.append((x_coor, y_coor))
                index += 1

    def x_ret(self):
        return self.xs

    def y_ret(self):
        return self.ys

    def change(self, ind):  # попадания мяча в блок
        if self.blocks[ind] == 3:
            self.blocks[ind] = 2
        elif self.blocks[ind] == 2:
            self.blocks[ind] = 1
        elif self.blocks[ind] == 1:
            self.blocks[ind] = 0

    def change_level(self, d):  # смена уровня и отрисовка новых платформ
        self.was.clear()
        if d == 1:
            self.blocks.clear()
            self.blocks = [1] * 30
        elif d == 2:
            self.blocks.clear()
            for _ in range(15):
                self.blocks.append(1)
                self.blocks.append(2)
            random.shuffle(self.blocks)
        elif d == 3:
            self.blocks.clear()
            for _ in range(10):
                self.blocks.append(1)
                self.blocks.append(2)
                self.blocks.append(3)
            random.shuffle(self.blocks)
        elif d == 4:
            self.blocks.clear()
            for _ in range(15):
                self.blocks.append(3)
                self.blocks.append(2)
            random.shuffle(self.blocks)


class Intro:
    def __init__(self, sc):  # загрузка кнопок на главном экране
        self.sc = sc
        self.start = pygame.image.load('data/start.png')
        self.exit = pygame.image.load('data/exit.png')
        self.rules = pygame.image.load('data/rules.png')
        self.controls = pygame.image.load('data/controls.png')

        self.sc_rect = self.sc.get_rect()
        self.start_rect = self.start.get_rect()
        self.exit_rect = self.exit.get_rect()
        self.rules_rect = self.rules.get_rect()
        self.controls_rect = self.controls.get_rect()

        self.start_rect.centerx = self.sc_rect.centerx
        self.exit_rect.centerx = self.sc_rect.centerx
        self.rules_rect.centerx = self.sc_rect.centerx
        self.controls_rect.centerx = self.sc_rect.centerx

        self.start_rect.y = 200
        self.rules_rect.y = 275
        self.controls_rect.y = 350
        self.exit_rect.y = 425


    def draw(self):
        self.sc.blit(self.start, self.start_rect)
        self.sc.blit(self.exit, self.exit_rect)
        self.sc.blit(self.rules, self.rules_rect)
        self.sc.blit(self.controls, self.controls_rect)


class End:  # загрузка конечного экрана и кнопок
    def __init__(self, sc):
        self.sc = sc
        self.replay = pygame.image.load('data/replay.png')
        self.exit = pygame.image.load('data/exit.png')
        self.menu = pygame.image.load('data/menu.png')

        self.sc_rect = self.sc.get_rect()
        self.replay_rect = self.replay.get_rect()
        self.exit_rect = self.exit.get_rect()
        self.menu_rect = self.menu.get_rect()

        self.replay_rect.centerx = self.sc_rect.centerx
        self.exit_rect.centerx = self.sc_rect.centerx
        self.menu_rect.centerx = self.sc_rect.centerx

        self.replay_rect.y = 200
        self.exit_rect.y = 350
        self.menu_rect.y = 275

    def draw(self):
        self.sc.blit(self.replay, self.replay_rect)
        self.sc.blit(self.exit, self.exit_rect)
        self.sc.blit(self.menu, self.menu_rect)


class Level:  # изменение уровня
    def __init__(self):
        self.level = 1

    def ret(self):
        return f'Уровень {self.level}'

    def change_level(self, lev):
        self.level = lev
        life.full_hearts()


class Lives:  # изменение жизней
    def __init__(self, sc):
        self.life = 3
        self.coords = [390, 425, 460]
        self.heart = pygame.image.load('data/heart.png')
        self.rect = self.heart.get_rect()
        self.sc = sc

    def ret(self):
        return self.life

    def change_level(self):
        self.life -= 1
        self.coords.remove(self.coords[0])

    def full_hearts(self):
        self.life = 3
        self.coords = [390, 425, 460]

    def hearts(self):  # рисование сердец
        self.rect.y = 20
        for lg in self.coords:
            self.rect.x = lg
            self.sc.blit(self.heart, self.rect)


class Back:  # кнопка назад
    def __init__(self, sc):
        self.sc = sc
        self.back = pygame.image.load('data/back.png')
        self.back_rect = self.back.get_rect()
        self.back_rect.x = 10
        self.back_rect.y = 440

    def draw(self):
        self.sc.blit(self.back, self.back_rect)


class Control:  # отрисовка кнопок в разделе controls
    def __init__(self, sc):
        self.sc = sc
        self.mouse = pygame.image.load('data/mouse.png')
        self.arrow = pygame.image.load('data/arrows.png')

        self.sc_rect = self.sc.get_rect()
        self.mouse_rect = self.mouse.get_rect()
        self.arrow_rect = self.arrow.get_rect()

        self.mouse_rect.centerx = self.sc_rect.centerx
        self.arrow_rect.centerx = self.sc_rect.centerx

        self.mouse_rect.y = 250
        self.arrow_rect.y = 350

    def draw(self):
        self.sc.blit(self.mouse, self.mouse_rect)
        self.sc.blit(self.arrow, self.arrow_rect)


class Firework:
    def __init__(self, sc):  # создание летящих искорок для концовок
        self.sc = sc
        self.coords = []
        self.colors = []
        for _ in range(500):
            color = random.randint(1, 4)
            x1 = random.randint(0, 495)
            y1 = random.randint(-2000, 0)
            self.colors.append(color)
            self.coords.append((x1, y1))

    def draw(self, stat):
        for t in range(len(self.coords)):
            if stat == 1:                       # цветные искорки
                if self.colors[t] == 1:
                    color = pygame.Color('red')
                elif self.colors[t] == 2:
                    color = pygame.Color('blue')
                elif self.colors[t] == 3:
                    color = pygame.Color('yellow')
                else:
                    color = pygame.Color('green')
            else:                               # серые искорки
                color = pygame.Color('grey')
            x2, y2 = self.coords[t]
            pygame.draw.rect(self.sc, color, (x2, y2, 10, 5))

    def move(self):  # движение искорок
        for t in range(len(self.coords)):
            x2, y2 = self.coords[t]
            y2 += 2
            c = random.randint(1, 5)
            if c == 5:
                x2 += 1
            elif c == 1:
                x2 -= 1
            self.coords[t] = (x2, y2)


if __name__ == '__main__':  # запуск программы
    pygame.init()
    size = width, height = 495, 500  # создание экрана
    pygame.display.set_caption('Мячик')
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((0, 0, 0))
    platform = Platform(screen)
    ball = Ball(screen)

    pygame.display.flip()
    check = False
    start = False
    clock = pygame.time.Clock()
    pos = (210, 290)
    blocks = []
    block = Blocks(screen)
    controls = Control(screen)

    rules_text = ["Правила:", "",                  # текст правил
                  "1. Для начала игры необходимо",
                  "    нажать на белую платформу.",
                  "2. Для управления платформой",
                  "    необходимо перемещать мышь",
                  "    или нажимать на стрелочки.",
                  "3. При вынесении курсора за",
                  "    пределы экрана платформа",
                  "    перестаёт двигаться.",
                  "4. Блоки ичсчезают:",
                  "    красный - с 3 ударов",
                  "    жёлтый - с 2 ударов",
                  "    зелёный - с 1 удара."]
    back = Back(screen)
    line2 = 'Мячик'
    fon = pygame.image.load('data/fon.jpg')        # загрузка фонового изображения
    screen.blit(fon, (0, 0))
    intr = Intro(screen)
    level = Level()
    life = Lives(screen)
    ending = End(screen)
    pygame.display.flip()
    game_start = False
    rules = False
    menu = True
    end = False
    mouse = True
    arrows = False
    left = False
    right = False
    control = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if 210 <= x <= 290 and 475 <= y <= 485 and game_start:    # проверка нажатия на платформу
                    check = True
                    start = True
                if 150 <= x <= 350 and control:  # выбор управления мышкой
                    if 250 <= y <= 300:
                        mouse = True
                        arrows = False
                    elif 350 <= y <= 400:        # выбор управления стрелками
                        mouse = False
                        arrows = True
                if 150 <= x <= 350 <= y <= 400:
                    if not game_start and not rules and not end and not control:  # проверка нажатия на "CONTROLS"
                        control = True
                        back.back = pygame.image.load('data/back.png')
                        menu = False
                    if end:
                        running = False
                if 150 <= x <= 350 and 425 <= y <= 475 and not game_start and not rules and not end and not control:
                    running = False
                if 150 <= x <= 350 and 275 <= y <= 350:
                    if not game_start and not rules and not end and not control:  # проверка нажатия на "RULES"
                        rules = True
                        back.back = pygame.image.load('data/back.png')
                        menu = False
                    elif end:                                    # проверка нажатия на "MENU"
                        menu = True
                        ending.menu = pygame.image.load('data/menu.png')
                        end = False
                        start = False
                        level.change_level(1)
                        block.change_level(1)
                if 10 <= x <= 60 and 440 <= y <= 490 and (rules or control):  # проверка нажатия на кнопку "назад"
                    rules = False
                    intr.rules = pygame.image.load('data/rules.png')
                    control = False
                    intr.controls = pygame.image.load('data/controls.png')
                    menu = True
                if 150 <= x <= 350 and 200 <= y <= 275:
                    if not game_start and not rules and not end and not control:  # проверка нажатия на "START"
                        game_start = True
                        menu = False
                    elif end:                                  # проверка нажатия на "REPLAY"
                        end = False
                        ending.replay = pygame.image.load('data/replay.png')
                        level.change_level(1)
                        block.change_level(1)
                        start = False
                        game_start = True
            if event.type == pygame.MOUSEMOTION:
                if check and mouse:                  # движение с помощью мыши
                    if pygame.mouse.get_focused():
                        pygame.mouse.set_visible(False)
                    a = event.pos[0]
                    if 40 <= a <= 455:
                        pos = (a - 40, a + 40)
                        platform.move(event.pos[0])
                if menu:                                   # движение мыши в меню
                    x, y = event.pos
                    if 150 <= x <= 350 <= y <= 400:
                        intr.controls = pygame.image.load('data/pale_controls.png')
                        intr.start = pygame.image.load('data/start.png')
                        intr.exit = pygame.image.load('data/exit.png')
                        intr.rules = pygame.image.load('data/rules.png')
                    elif 150 <= x <= 350 and 275 <= y <= 325:
                        intr.rules = pygame.image.load('data/pale_rules.png')
                        intr.start = pygame.image.load('data/start.png')
                        intr.exit = pygame.image.load('data/exit.png')
                        intr.controls = pygame.image.load('data/controls.png')
                    elif 150 <= x <= 350 and 200 <= y <= 255:
                        intr.start = pygame.image.load('data/pale_start.png')
                        intr.exit = pygame.image.load('data/exit.png')
                        intr.rules = pygame.image.load('data/rules.png')
                        intr.controls = pygame.image.load('data/controls.png')
                    elif 150 <= x <= 350 and 425 <= y <= 455:
                        intr.exit = pygame.image.load('data/pale_exit.png')
                        intr.start = pygame.image.load('data/start.png')
                        intr.rules = pygame.image.load('data/rules.png')
                        intr.controls = pygame.image.load('data/controls.png')
                    else:
                        intr.start = pygame.image.load('data/start.png')
                        intr.exit = pygame.image.load('data/exit.png')
                        intr.rules = pygame.image.load('data/rules.png')
                        intr.controls = pygame.image.load('data/controls.png')
                if end:                                     # движение мыши на конечном экране
                    x, y = event.pos
                    if 150 <= x <= 350 and 200 <= y <= 255:
                        ending.replay = pygame.image.load('data/pale_replay.png')
                        ending.exit = pygame.image.load('data/exit.png')
                        ending.menu = pygame.image.load('data/menu.png')
                    elif 150 <= x <= 350 and 275 <= y <= 325:
                        ending.replay = pygame.image.load('data/replay.png')
                        ending.exit = pygame.image.load('data/exit.png')
                        ending.menu = pygame.image.load('data/pale_menu.png')
                    elif 150 <= x <= 350 <= y <= 400:
                        ending.replay = pygame.image.load('data/replay.png')
                        ending.exit = pygame.image.load('data/pale_exit.png')
                        ending.menu = pygame.image.load('data/menu.png')
                    else:
                        ending.replay = pygame.image.load('data/replay.png')
                        ending.exit = pygame.image.load('data/exit.png')
                        ending.menu = pygame.image.load('data/menu.png')
                if control:                       # движение мыши в разделе controls
                    x, y = event.pos
                    if 150 <= x <= 350 and 250 <= y <= 300:
                        controls.mouse = pygame.image.load('data/pale_mouse.png')
                        back.back = pygame.image.load('data/back.png')
                        if not arrows:
                            controls.arrow = pygame.image.load('data/arrows.png')
                    elif 150 <= x <= 350 <= y <= 400:
                        if not mouse:
                            controls.mouse = pygame.image.load('data/mouse.png')
                        back.back = pygame.image.load('data/back.png')
                        controls.arrow = pygame.image.load('data/pale_arrows.png')
                    elif 10 <= x <= 60 and 440 <= y <= 490:
                        back.back = pygame.image.load('data/pale_back.png')
                    else:
                        back.back = pygame.image.load('data/back.png')
                        if mouse:
                            controls.mouse = pygame.image.load('data/pale_mouse.png')
                            controls.arrow = pygame.image.load('data/arrows.png')
                        elif arrows:
                            controls.mouse = pygame.image.load('data/mouse.png')
                            controls.arrow = pygame.image.load('data/pale_arrows.png')
                if rules:                                         # движения мыши в разделе rules
                    x, y = event.pos
                    if 10 <= x <= 60 and 440 <= y <= 490:
                        back.back = pygame.image.load('data/pale_back.png')
                    back.back = pygame.image.load('data/back.png')

            if event.type == pygame.KEYDOWN and check and arrows:   # движение с помощью стрелок
                if pygame.mouse.get_focused():
                    pygame.mouse.set_visible(False)
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
            if event.type == pygame.KEYUP and check and arrows:
                if pygame.mouse.get_focused():
                    pygame.mouse.set_visible(False)
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
        if right:
            platform.right()
        if left:
            platform.left()
        if len(block.was) == 30:
            start = False
            check = False
            left = False
            right = False
            if level.level == 1:
                level.change_level(2)
                block.change_level(2)
            elif level.level == 2:
                level.change_level(3)
                block.change_level(3)
            elif level.level == 3:
                level.change_level(4)
                block.change_level(4)
            elif level.level == 4:
                end = True
        if control:  # раздел controls
            screen.blit(fon, (0, 0))
            if mouse:
                text = 'Контроль платформы: мышь'
            else:
                text = 'Контроль платформы: стрелки'
            font = pygame.font.Font(None, 40)
            string_rendered = font.render(text, True, (221, 160, 221))
            end_rect = string_rendered.get_rect()
            end_rect.top = 70
            end_rect.x = 250 - (end_rect.width / 2)
            screen.blit(string_rendered, end_rect)
            controls.draw()
            back.draw()
            pygame.display.flip()
        if life.life == 0:
            end = True
        if end:  # конечный экран
            game_start = False
            right = False
            left = False
            screen.fill((0, 0, 0))
            if life.life == 0:
                text = 'ПРОИГРЫШ! :('
                fire = Firework(screen)
                fire.draw(0)
            else:
                fire = Firework(screen)
                fire.draw(1)
                text = 'ПОБЕДА! :)'
            fire.move()
            ending.draw()
            font = pygame.font.Font(None, 70)
            string_rendered = font.render(text, True, (221, 160, 221))
            end_rect = string_rendered.get_rect()
            end_rect.top = 70
            end_rect.x = 250 - (end_rect.width / 2)
            screen.blit(string_rendered, end_rect)
            pygame.display.flip()

        if rules:                                  # правила игры
            screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 30)
            text_coord = 30
            n = 0
            for line in rules_text:                # вывод правил
                if n == 0:
                    font = pygame.font.Font(None, 50)
                    n = 1
                elif n == 1:
                    font = pygame.font.Font(None, 30)
                string_rendered = font.render(line, True, (230, 230, 250))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 88
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
            back.draw()
            pygame.display.flip()

        if menu:                                   # главное меню
            screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 70)
            string_rendered = font.render(line2, True, (221, 160, 221))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 70
            intro_rect.x = 250 - (intro_rect.width / 2)
            screen.blit(string_rendered, intro_rect)
            intr.draw()
            pygame.display.flip()

        if game_start:                             # начало игры
            level_text = level.ret()
            font = pygame.font.Font(None, 30)
            string_rendered = font.render(level_text, True, (255, 255, 255))
            level_rect = string_rendered.get_rect()
            level_rect.top = 20
            level_rect.x = 10
            if check:
                ball.move(platform.rect.x)
                start = ball.check()
            if not start:  # обновление платформы и шарика
                check = False
                left = False
                right = False
                platform.rect.centerx = 250
                ball.rect.centerx = 250
                ball.rect.centery = 465
                pygame.mouse.set_visible(True)
                ball.x = '-'
                ball.y = '-'
            screen.fill((0, 0, 0))
            screen.blit(string_rendered, level_rect)
            life.hearts()
            block.draw()
            ball.draw()
            platform.draw()
            pygame.display.update()

    exit()
