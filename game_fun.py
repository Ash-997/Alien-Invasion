import sys  # if we are creating instance inside the function
import pygame  # the instance parameter must be included in  function
from bull import Bullet
from alien import Alien
from time import sleep
from button import Button
from boat import Boat


def check_event(ai_setting,screen,stats,sb, play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         sys.exit()
        elif event.type == pygame.KEYDOWN:
          check_keydown_events(event, ai_setting, ship, screen, bullets)
        elif event.type == pygame.KEYUP:
          check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = pygame.mouse.get_pos()
             check_play_button(ai_setting,screen,stats,sb, play_button,ship,aliens,bullets, mouse_x, mouse_y)

def check_play_button(ai_setting,screen,stats,sb, play_button,ship,aliens,bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_setting.initialize_dynamic_setting()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
def check_keydown_events(event, ai_setting, ship, screen, bullets):  # here check_keydown_events
    if event.key == pygame.K_RIGHT:  # carries the fire_bullet funnction
        ship.moving_right = True  # argument because we never callled
    if event.key == pygame.K_LEFT:  # fire_ bullet function directyl
        ship.moving_left = True  # therefore deleting argument in
    elif event.key == pygame.K_SPACE:  # check_keydown_events cause error
        fire_bullet(ai_setting, screen, ship, bullets)  # because its unable to supply
        # necessary arugment to the function
        # which is inside it


# elif event.type == pygame.KEYUP:

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def get_number_alien_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_setting, ship_height, alien_height):
    available_space_y = (ai_setting.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_setting, screen, ship, aliens):
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_alien_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def ship_hit(ai_setting, stats, screen,sb, ship, aliens, bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_setting, stats,sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats,sb, screen, ship, aliens, bullets)
            break


def update_aliens(ai_setting, stats,sb, screen, ship, aliens, bullets):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats,screen, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_setting, stats,sb, screen, ship, aliens, bullets)

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        #sb.prep_high_score()
        with open("high_score.txt","w") as hs:
            hs.write(str(stats.high_score))
        sb.prep_high_score()


def update_bullet(ai_setting, screen,stats,sb, ship, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_setting, screen, ship, aliens)
    check_alien_bullet_collosion(ai_setting, screen, stats, sb, ship, bullets, aliens)

def check_alien_bullet_collosion(ai_setting, screen,stats,sb, ship, bullets, aliens):
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision:
        for aliens1 in collision.values():
            stats.score += ai_setting.alien_point * len(aliens1)
           # stats.score += ai_setting.alien_point
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_setting, screen, ship, aliens)


def update_screen(ai_setting, screen, stats,sb, ship, aliens, bullets,play_button):  # function parameter are not so important

    screen.blit(ai_setting.bg, (0, 0))  # function argument when we call it is important
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # balien.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
