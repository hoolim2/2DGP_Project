import random
import game_framework
import title_state
import gameover_state

from pico2d import *
name = "MainState"

class Background:
    def __init__(self):
        self.soundloudness=64
        self.backgroundimage = load_image('resource\\background.png')
        self.backgroundhardimage = load_image('resource\\background_hard.png')
        self.image = load_image('resource\\background.png')
        self.BG_sound = load_music('resource\\music\\mainTheme.mp3')
        self.BG_sound.set_volume(self.soundloudness)

        self.BG_sound.repeat_play()

    def update(self,frame_time):
        self.soundloudness -= 1
        self.BG_sound.set_volume(self.soundloudness)

    def draw(self):
        global totalScore
        self.backgroundimage.draw(640, 360)
        if totalScore>1000:
            self.backgroundhardimage.draw(640, 360)

#cahracter class=======================

class characterFirstLine:
    def __init__(self):
        self.x, self.y = 640 - lineFirstCharSize / 2, 100
        self.dir=1
        self.flyspdX = 1500
        self.flyspdY = 500 * random.randrange(1, 5)
        self.delayTime = 0
        self.image = load_image('resource\\hero_sprite.png')

    def update(self,frame_time):
        #Idle
        global animationIsPlaying, damagePlay,lineFirstCharSize, right_key_down, left_key_down, up_key_down,x_key_down,lineFirstNumX,lineFirstNumY,explosion,totalScore
        if animationIsPlaying==False:
            self.x += self.dir
            if damagePlay == True:
                lineFirstCharSize = 400
                self.x = 640 - lineFirstCharSize / 2
            elif damagePlay == False:
                lineFirstCharSize = 220
            if self.x >= (640-lineFirstCharSize/2)+5:
                self.x= (640 - lineFirstCharSize / 2) + 5
                self.dir = -10*frame_time
            elif self.x <= (640-lineFirstCharSize/2)-5:
                self.x= (640 - lineFirstCharSize / 2) - 5
                self.dir = 10*frame_time
        #play Anmation
        elif animationIsPlaying==True:
            self.delayTime+=frame_time
            if up_key_down == True and self.delayTime>0.8:
                self.y += self.flyspdX * frame_time
            if self.delayTime > 0.7:
                if right_key_down == True:
                    self.x += self.flyspdX*frame_time
                    self.y += self.flyspdY * frame_time
                    self.flyspdY -= 5000 * frame_time
                elif left_key_down == True:
                    self.x -= self.flyspdX*frame_time
                    self.y += self.flyspdY * frame_time
                    self.flyspdY -= 5000 * frame_time
            if x_key_down == True and self.delayTime > 2.5:
                explosion=True
                self.x += self.flyspdX * frame_time
                self.y += self.flyspdY * frame_time
        #Reset
            if self.x > 1280 or self.x < 0-lineFirstCharSize or self.y > 720:
                if explosion==False:
                    animationIsPlaying = False
                    right_key_down = False
                    left_key_down = False
                    up_key_down = False
                    x_key_down =False
                    explosion=False
                    self.x, self.y = 640 - lineFirstCharSize / 2, 100
                    self.flyspdY= 500 * random.randrange(3, 6)
                    self.delayTime=0
                    characterChanger(1)
            if self.delayTime>5:
                animationIsPlaying = False
                right_key_down = False
                left_key_down = False
                up_key_down = False
                x_key_down = False
                totalScore+=80
                self.x, self.y = 640 - lineFirstCharSize / 2, 100
                self.flyspdY = 500 * random.randrange(3, 6)
                self.delayTime = 0
                characterChanger(1)
                explosion = False

    def draw(self):
        self.image.clip_draw_to_origin(lineFirstNumX * characterImageSize, lineFirstNumY * characterImageSize, characterImageSize, characterImageSize, self.x, self.y, lineFirstCharSize, lineFirstCharSize)

class characterSecondLine:
    def __init__(self):
        self.x, self.y = 640 - lineSecondCharSize / 2, 200
        self.flyspd = 500*random.randrange(1, 5)
        self.dir=-1
        self.image = load_image('resource\\hero_sprite.png')

    def update(self,frame_time):
        if explosion==True:
            self.x -= 1500 * frame_time
            self.y += self.flyspd * frame_time
        elif explosion==False:
            self.y=200
            self.x += self.dir
            self.flyspd = 500 * random.randrange(1, 5)
            if self.x >= (640-lineSecondCharSize/2)+3:
                self.x= (640 - lineSecondCharSize / 2) + 3
                self.dir = -5*frame_time
            elif self.x <= (640-lineSecondCharSize/2)-3:
                self.x= (640 - lineSecondCharSize / 2) - 3
                self.dir = 5*frame_time

    def draw(self):
        self.image.clip_draw_to_origin(lineSecondNumX * characterImageSize, lineSecondNumY * characterImageSize, characterImageSize, characterImageSize, self.x, self.y, lineSecondCharSize, lineSecondCharSize)

class characterThirdLine:
    def __init__(self):
        self.x = 640 - lineThirdCharSize / 2
        self.y =250
        self.dir=-1
        self.image = load_image('resource\\hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x > (640-lineThirdCharSize/2)+1:
            self.x=(640-lineThirdCharSize/2)+1
            self.dir = -2*frame_time
        elif self.x < (640-lineThirdCharSize/2)-1:
            self.x=(640-lineThirdCharSize/2)-1
            self.dir = 2*frame_time
        pass

    def draw(self):
        self.image.clip_draw_to_origin(lineThirdNumX * characterImageSize, lineThirdNumY * characterImageSize, characterImageSize, characterImageSize, self.x, self.y, lineThirdCharSize, lineThirdCharSize)

class characterForthLine:
    def __init__(self):
        self.x = 640 - lineForthCharSize / 2
        self.y =300
        self.dir=1
        self.image = load_image('resource\\hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x > (640-lineForthCharSize/2)+1:
            self.x=(640-lineForthCharSize/2)+1
            self.dir = -2*frame_time
        elif self.x < (640-lineForthCharSize/2)-1:
            self.x =(640-lineForthCharSize/2)-1
            self.dir = 2*frame_time
        pass

    def draw(self):
        self.image.clip_draw_to_origin(lineForthNumX * characterImageSize, lineForthNumY * characterImageSize, characterImageSize, characterImageSize, self.x, self.y, lineForthCharSize, lineForthCharSize)

class characterFifthLine:
    global changeSign
    def __init__(self):
        self.x = 640 - lineFifthCharSize / 2
        self.y =330
        self.dir=-1
        self.image = load_image('resource\\hero_sprite.png')

    def update(self,frame_time):
        self.x += self.dir
        if self.x > (640-lineFifthCharSize/2)+1:
            self.x =(640-lineFifthCharSize/2)+1
            self.dir = -1*frame_time
        elif self.x < (640-lineFifthCharSize/2)-1:
            self.x =(640-lineFifthCharSize/2)-1
            self.dir = 1*frame_time

    def draw(self):
        self.image.clip_draw_to_origin(lineFifthNumX * characterImageSize, lineFifthNumY * characterImageSize, characterImageSize, characterImageSize, self.x, self.y, lineFifthCharSize, lineFifthCharSize)

#UI class==========================================================================
class uiHeart:
    def __init__(self):
        self.x,self.y=50,600
        self.HP = userHP
        self.size=120
        self.dir=0.2
        self.image = load_image('resource\\heart.png')

    def update(self):
        self.HP = userHP
        self.x -= self.dir/2
        self.y -= self.dir/2
        self.size += self.dir
        if self.size<=120:
            self.dir=0.8
        if self.size>=130:
            self.dir= -0.5

    def draw(self):
        if (self.HP >= 1):
            self.image.clip_draw_to_origin(0, 0, 512, 512, self.x, self.y,self.size ,self.size)
            if (self.HP >= 2):
                self.image.clip_draw_to_origin(0, 0, 512, 512, self.x + 70, self.y, self.size, self.size)
                if (self.HP >= 3):
                    self.image.clip_draw_to_origin(0, 0, 512, 512, self.x + 140, self.y, self.size, self.size)
        elif (self.HP <= 0):
            pass

class uiDialogueText:
    global characterType

    def __init__(self):
        self.image=None
        characterType = characterTypeGetter()
        if self.image==None:
            if characterType==0:
                self.image = load_image('dialogue\\%d.png'%random.randint(1, 10))
            elif characterType==1:
                self.image = load_image('dialogue\\%d.png' % random.randint(11, 20))
            elif characterType==2:
                self.image = load_image('dialogue\\%d.png' % random.randint(21, 30))
            else:
                self.image = load_image('dialogue\\0.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640,530,720,200)

class uiDialogueBox:
    def __init__(self):
        self.image = load_image('resource\\dialogue.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640,500,720,226)

class uiFadeout:
    def __init__(self):
        self.playanimation=0
        self.Yframes = 3
        self.play_frames = 0
        self.framepass = 0
        self.image = load_image('resource\\black_fadeout.png')

    def update(self,frame_time):
        self.playanimation+=frame_time
        if self.framepass>=7:
            self.play_frames = (self.play_frames + 1) % 5
            self.framepass=0
            if self.play_frames==0:
                self.Yframes -=1
        self.framepass += 1
        if self.playanimation>=1.5:
            self.Yframes = 3
            self.play_frames=0
            self.playdamage = 0

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 0, -280, 1280, 1280)

class uiTimeGauge:
    def __init__(self):
        self.timeamount=-0.2
        self.image = load_image('resource\\ui_timegauge.png')
        self.barimage =load_image('resource\\ui_timegaugebar.png')

    def update(self,frametime):
        if animationIsPlaying == True or damagePlay == True:
            self.timeamount = 0.0
        self.timeamount+=float(frametime)/globalTimelimit
        print(self.timeamount)
        if(self.timeamount>1 and self.timeamount<1.2):
            effectsound.soundHitPlay()
            haveDamage()
            self.timeamount=0.0
        elif(self.timeamount>1.2):
            self.timeamount = 0.0
        pass

    def draw(self):
        if animationIsPlaying == False and damagePlay == False:
            self.barimage.clip_draw_to_origin(0, 0, 251, 21,541,390,251-((self.timeamount)*251),21)
            self.image.draw(640, 400, 316, 21)

#effect class=========================================================================

class damageEffect:
    def __init__(self):
        self.playdamage=0
        self.Yframes = 3
        self.play_frames = 0
        self.framepass = 0
        self.image = load_image('resource\\damage.png')

    def update(self,frame_time):
        global damagePlay,lineFirstNumX,lineFirstNumY
        if damagePlay==True:
            self.playdamage+=frame_time
            if self.framepass>=3:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
            if self.playdamage>=1:
                damagePlay=False
                self.Yframes = 3
                self.play_frames=0
                self.playdamage = 0
                characterChanger(0)

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 0, -280, 1280, 1280)

class slashEffect:

    def __init__(self):
        self.Yframes = 4
        self.play_frames = 0
        self.framepass=0
        self.image = load_image('resource\\fx_slash.png')

    def update(self):
        if animationIsPlaying==True:
            if left_key_down == True:
                if self.framepass>=2:
                    self.play_frames = (self.play_frames + 1) % 5
                    self.framepass=0
                    if self.play_frames==0:
                        if self.Yframes>0:
                            effectsound.soundSlashPlay()
                        self.Yframes -=1
                self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 4

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 390, -50, 500, 500)

class slashadEffect:

    def __init__(self):
        self.Yframes = 6
        self.play_frames = 0
        self.framepass=0
        self.image = load_image('resource\\fx_slashadvence.png')

    def update(self):
        if animationIsPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 6

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames * 192, self.Yframes * 192, 192, 192, 390, -50, 500, 500)

class magicEffect:

    def __init__(self):
        self.Yframes = 5
        self.play_frames = 0
        self.framepass=0
        self.image = load_image('resource\\fx_magic.png')

    def update(self):
        if animationIsPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 5

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class drainEffect:

    def __init__(self):
        self.Yframes = 5
        self.play_frames = 0
        self.framepass = 0
        self.image = load_image('resource\\fx_darkness.png')

    def update(self):
        if animationIsPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 5

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class healEffect:

    def __init__(self):
        self.Yframes = 5
        self.play_frames = 0
        self.framepass =0
        self.image = load_image('resource\\fx_heal.png')

    def update(self):
        if animationIsPlaying==True:
            if self.framepass>=4:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 5

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class bloodEffect:

    def __init__(self):
        self.Yframes = 10
        self.play_frames = 0
        self.framepass =0
        self.image = load_image('resource\\fx_blood.png')

    def update(self):
        if animationIsPlaying==True:
            if self.framepass>=2:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 10

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,390,-50,500,500)

class blessEffect:

    def __init__(self):
        self.Yframes = 9
        self.play_frames = 0
        self.framepass =0
        self.image = load_image('resource\\fx_bless.png')

    def update(self):
        if animationIsPlaying==True:
            if self.framepass>=7:
                self.play_frames = (self.play_frames + 1) % 5
                self.framepass=0
                if self.play_frames==0:
                    self.Yframes -=1
            self.framepass += 1
        if animationIsPlaying==False:
            self.play_frames = 0
            self.Yframes = 9

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*192, self.Yframes*192,192,192,0,-350,1280,1280)

class explosionEffect:

    def __init__(self):
        self.Yframes = 12
        self.play_frames = 0
        self.framepass =0
        self.image = load_image('resource\\fx_explosion.png')

    def update(self):
        if right_key_down==False and up_key_down==False and left_key_down==False:
            if animationIsPlaying==True:
                if self.framepass>=6:
                    self.play_frames = (self.play_frames + 1) % 4
                    self.framepass=0
                    if self.play_frames==0:
                        if self.Yframes==12:
                            effectsound.soundLightningPlay()
                        elif self.Yframes==8:
                            effectsound.soundFlashPlay()
                        elif self.Yframes==7:
                            effectsound.soundExplosionPlay()
                        self.Yframes -=1
                self.framepass += 1
            if animationIsPlaying==False:
                self.play_frames = 0
                self.Yframes = 12

    def draw(self):
        self.image.clip_draw_to_origin(self.play_frames*512, self.Yframes*288,512,288,0,0,1280,720)

class effectSound:
    soundMagic=None
    soundExact=None
    soundExplosion=None
    soundFlash=None
    soundHeal=None
    soundHit=None
    soundLightning=None
    soundSlash=None
    def __init__(self):
        if effectSound.soundMagic == None:
            effectSound.soundMagic = load_wav('resource\\music\\soundMagic.wav')
            effectSound.soundMagic.set_volume(125)
        if effectSound.soundExact == None:
            effectSound.soundExact = load_wav('resource\\music\\soundExact.wav')
            effectSound.soundExact.set_volume(44)
        if effectSound.soundExplosion == None:
            effectSound.soundExplosion = load_wav('resource\\music\\soundExplosion.wav')
            effectSound.soundExplosion.set_volume(64)
        if effectSound.soundFlash == None:
            effectSound.soundFlash = load_wav('resource\\music\\soundFlash.wav')
            effectSound.soundFlash.set_volume(64)
        if effectSound.soundHeal == None:
            effectSound.soundHeal = load_wav('resource\\music\\soundHeal.wav')
            effectSound.soundHeal.set_volume(64)
        if effectSound.soundHit == None:
            effectSound.soundHit = load_wav('resource\\music\\soundHit.wav')
            effectSound.soundHit.set_volume(64)
        if effectSound.soundLightning == None:
            effectSound.soundLightning = load_wav('resource\\music\\soundLightning.wav')
            effectSound.soundLightning.set_volume(64)
        if effectSound.soundSlash == None:
            effectSound.soundSlash = load_wav('resource\\music\\soundSlash.wav')
            effectSound.soundSlash.set_volume(64)

    def soundMagicPlay(self):
        effectSound.soundMagic.play()

    def soundExactPlay(self):
        effectSound.soundExact.play()

    def soundExplosionPlay(self):
        effectSound.soundExplosion.play()

    def soundFlashPlay(self):
        effectSound.soundFlash.play()

    def soundHealPlay(self):
        effectSound.soundHeal.play()

    def soundHitPlay(self):
        effectSound.soundHit.play()

    def soundLightningPlay(self):
        effectSound.soundLightning.play()

    def soundSlashPlay(self):
        effectSound.soundSlash.play()


#=====================================================

def enter():
    global background,lineFirst,lineSecond,lineThird,lineForth,lineFifth,slash_fx,magic_fx,heal_fx,drain_fx,slashad_fx,blood_fx,heart,damage_fx,dialogue,ui_Text,bless_fx,explosion_fx,score_ui,fadeout_fx,uitimegauge
    global right_key_down,left_key_down,up_key_down,x_key_down,animationIsPlaying,damagePlay,explosion,interrogationFlag,characterType
    global lineFirstNumX,lineSecondNumX,lineThirdNumX, lineForthNumX,lineFifthNumX,lineFirstNumY, lineSecondNumY, lineThirdNumY, lineForthNumY,lineFifthNumY
    global characterImageSize,lineFirstCharSize,lineSecondCharSize,lineThirdCharSize,lineForthCharSize,lineFifthCharSize,typeKnight,typeMagician,typeCitizen,userHP,totalScore,current_time,gameovertime,globalTimelimit
    global effectsound,timeamount,font

    right_key_down = False
    left_key_down = False
    up_key_down = False
    x_key_down = False
    animationIsPlaying = False
    damagePlay = False
    explosion = False
    interrogationFlag = False

    font = None

    if font == None:
        font=load_font('resource\\Typo_MoonFlowerM.TTF', 60)

    lineFirst = None
    lineSecond = None
    lineThird = None
    lineForth = None
    lineFifth = None
    background = None
    ui_Text = None
    characterType = -1
    gameovertime = 0
    globalTimelimit=10

    # Generate====================
    lineFirstNumX, lineSecondNumX, lineThirdNumX, lineForthNumX = -1, -1, -1, -1
    lineFirstNumY, lineSecondNumY, lineThirdNumY, lineForthNumY = -1, -1, -1, -1
    lineFifthNumX = random.randint(0, 11)
    lineFifthNumY = random.randint(0, 7)

    characterImageSize = 53
    lineFirstCharSize = 220
    lineSecondCharSize = 160
    lineThirdCharSize = 130
    lineForthCharSize = 105
    lineFifthCharSize = 95
    # ====================

    typeKnight = 0
    typeMagician = 1
    typeCitizen = 2
    userHP = 3
    totalScore = 0
    current_time = 0.0

    ui_Text = None
    characterGenerator()
    lineFirst = characterFirstLine()
    lineSecond = characterSecondLine()
    lineThird = characterThirdLine()
    lineForth = characterForthLine()
    lineFifth = characterFifthLine()
    slash_fx = slashEffect()
    slashad_fx = slashadEffect()
    magic_fx = magicEffect()
    heal_fx= healEffect()
    drain_fx= drainEffect()
    blood_fx = bloodEffect()
    heart = uiHeart()
    damage_fx = damageEffect()
    bless_fx= blessEffect()
    explosion_fx=explosionEffect()
    fadeout_fx= uiFadeout()

    dialogue=uiDialogueBox()
    uitimegauge=uiTimeGauge()
    background = Background()

    effectsound=effectSound()

    print('all resource is initialized..')
    pass


def exit():
    global background,lineFirst,lineSecond,lineThird,lineForth,lineFifth,slash_fx,magic_fx,heal_fx,drain_fx,slashad_fx,blood_fx,heart,damage_fx,dialogue,ui_Text,bless_fx,explosion_fx,fadeout_fx,effectsound
    del(background)
    del(lineFirst)
    del(lineSecond)
    del(lineThird)
    del(lineForth)
    del (lineFifth)
    del (slash_fx)
    del (magic_fx)
    del (heal_fx)
    del(drain_fx)
    del (blood_fx)
    del (heart)
    del (damage_fx)
    del (dialogue)
    del (ui_Text)
    del (fadeout_fx)
    del (effectsound)
    pass


def pause():
    pass


def resume():
    pass

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def handle_events():
    global right_key_down,left_key_down,up_key_down,x_key_down,animationIsPlaying
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            Interrogation()
        if animationIsPlaying == False:
            if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                attackJudge(typeKnight)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                attackJudge(typeMagician)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                attackJudge(typeCitizen)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_m:
                x_key_down = True
                animationIsPlaying = True
    pass

def update():
    global gameovertime,globalTimelimit

    characterGenerator()
    frame_time=get_frame_time()
    lineFirst.update(frame_time)
    lineSecond.update(frame_time)
    lineThird.update(frame_time)
    lineForth.update(frame_time)
    lineFifth.update(frame_time)
    slash_fx.update()
    slashad_fx.update()
    magic_fx.update()
    heal_fx.update()
    drain_fx.update()
    blood_fx.update()
    heart.update()
    bless_fx.update()
    explosion_fx.update()
    damage_fx.update(frame_time)
    uitimegauge.update(frame_time)
    if userHP <=0:
        fadeout_fx.update(frame_time)
        background.update(frame_time)
        gameovertime+=frame_time
        if gameovertime >= 1.5:
            game_framework.change_state(gameover_state)

    pass


def draw():
    global totalScore
    clear_canvas()
    background.draw()
    #characterdraw------------------
    lineFifth.draw()
    lineForth.draw()
    lineThird.draw()
    lineSecond.draw()
    lineFirst.draw()
    #fxdraw-------------------
    if left_key_down == True:
        if animationIsPlaying == True:
            blood_fx.draw()
            slash_fx.draw()
            slashad_fx.draw()

    if right_key_down == True:
        if animationIsPlaying==True:
            blood_fx.draw()
            drain_fx.draw()
            magic_fx.draw()

    if up_key_down == True:
        if animationIsPlaying == True:
            heal_fx.draw()

    if x_key_down == True:
        if animationIsPlaying == True:
            blood_fx.draw()
            bless_fx.draw()
            explosion_fx.draw()
    #uidraw-----------------
    heart.draw()
    uitimegauge.draw()
    if interrogationFlag==True:
        dialogue.draw()
        ui_Text.draw()
    if damagePlay==True:
        damage_fx.draw()
    if userHP <= 0:
        fadeout_fx.draw()

    drawScore = totalScore
    font.draw(950, 650, 'Score: %d' % (int(drawScore)), (255,255, 255))
    #--------------------------

    update_canvas()

    delay(0.01)
    pass

def characterGenerator():
    global lineFirstNumX,lineSecondNumX,lineThirdNumX,lineForthNumX,lineFifthNumX
    global lineFirstNumY,lineSecondNumY,lineThirdNumY,lineForthNumY,lineFifthNumY
    global totalScore,characterType,ui_Text
    if(lineFirstNumX == -1):
        lineFirstNumX = lineSecondNumX
        lineFirstNumY = lineSecondNumY
        lineSecondNumX=-1
        lineSecondNumY=-1
        if ui_Text==None and lineFirstNumX != -1:
            ui_Text = uiDialogueText()
    if (lineSecondNumX == -1):
        lineSecondNumX = lineThirdNumX
        lineSecondNumY = lineThirdNumY
        lineThirdNumX = -1
        lineThirdNumY = -1
    if (lineThirdNumX == -1):
        lineThirdNumX = lineForthNumX
        lineThirdNumY = lineForthNumY
        lineForthNumX = -1
        lineForthNumY = -1
    if (lineForthNumX == -1):
        lineForthNumX = lineFifthNumX
        lineForthNumY = lineFifthNumY
        lineFifthNumX = -1
        lineFifthNumY = -1
    if (lineFifthNumX == -1):
        lineFifthNumX = random.randrange(0, 11)
        lineFifthNumY = random.randrange(0, 7)

def Interrogation():
    global interrogationFlag
    interrogationFlag=True

def haveDamage():
    global userHP,damagePlay
    if damagePlay== False:
        userHP-=1
        damagePlay=True

def characterChanger(exactsign):
    global interrogationFlag,lineFirstNumX,lineFirstNumY,lineSecondNumX,lineSecondNumY,ui_Text,userHP,globalTimelimit,totalScore
    interrogationFlag = False
    if(exactsign==1):
        totalScore += 50
        globalTimelimit -=1
        if globalTimelimit < 1:
            globalTimelimit = 1.0
        effectsound.soundExactPlay()
    lineFirstNumX = -1
    lineFirstNumY = -1
    if explosion==True:
        totalScore += 370
        lineSecondNumX = -1
        lineSecondNumY = -1
    del (ui_Text)
    ui_Text = None

def characterTypeGetter():
    global lineFirstNumX,lineFirstNumY

    charNumY = lineFirstNumX
    charNumX = lineFirstNumY

    if charNumX==0:
        print('call:', (charNumX, charNumY))
        if charNumY==0 or charNumY==1 or charNumY==2 or charNumY==3 or charNumY==6 or charNumY==7 or charNumY==9 or charNumY==10:
            return typeKnight #Type 'knight'
        elif charNumY == 8:
            return typeCitizen #Type 'citizen'
        else:
            return typeMagician #Type 'magician'
    elif charNumX==1:
        print('call:', (charNumX, charNumY))
        if charNumY==0 or charNumY== 5 or charNumY== 6 or charNumY== 7 or charNumY==11:
            return typeKnight
        elif charNumY == 1 or charNumY==3 or charNumY==4 or charNumY==8:
            return typeCitizen
        else:
            return typeMagician
    elif charNumX==2:
        print('call:', (charNumX, charNumY))
        if charNumY==1 or charNumY==3 or charNumY==9 or charNumY==11:
            return typeKnight
        elif charNumY == 5 or charNumY==6 or charNumY==10:
            return typeCitizen
        else:
            return typeMagician
    elif charNumX==3:
        print('call:', (charNumX, charNumY))
        if charNumY==3 or charNumY==4 or charNumY==8 or charNumY==9 or charNumY==10:
            return typeKnight
        elif charNumY == 1 or charNumY==6 or charNumY==11:
            return typeCitizen
        else:
            return typeMagician
    elif charNumX==4:
        print('call:', (charNumX, charNumY))
        if charNumY==0 or charNumY==1 or charNumY==2 or charNumY==5 or charNumY==6 or charNumY==7 or charNumY==8 or charNumY==10 or charNumY==11:
            return typeKnight
        elif charNumY == 4:
            return typeCitizen
        else:
            return typeMagician
    elif charNumX==5:
        print('call:', (charNumX, charNumY))
        if charNumY==0 or charNumY==1 or charNumY==2 or charNumY==3 or charNumY==5 or charNumY==6 or charNumY==7 or charNumY==10 or charNumY==11:
            return typeKnight
        elif charNumY == 9:
            return typeCitizen
        else:
            return typeMagician
    elif charNumX==6:
        print('call:', (charNumX, charNumY))
        if charNumY==3 or charNumY==4 or charNumY==5 or charNumY==7 or charNumY==8:
            return typeKnight
        elif charNumY == 1 or charNumY==6 or charNumY==10 or charNumY==11:
            return typeCitizen
        else:
            return typeMagician
    elif charNumX==7:
        print('call:', (charNumX, charNumY))
        if charNumY==0 or charNumY==9 or charNumY==11:
            return typeKnight
        elif charNumY == 3 or charNumY==6 or charNumY==7 or charNumY==8:
            return typeCitizen
        else:
            return typeMagician

def attackJudge(attackType):
    global characterType,right_key_down,left_key_down,up_key_down,animationIsPlaying
    attackType=int(attackType)
    print(attackType)
    if characterTypeGetter() == attackType:
        print('same')
        if attackType==typeKnight:
            effectsound.soundMagicPlay()
            right_key_down = True
            animationIsPlaying = True
        elif attackType == typeCitizen:
            effectsound.soundHealPlay()
            up_key_down = True
            animationIsPlaying = True
        elif attackType == typeMagician:
            left_key_down = True
            animationIsPlaying = True
    else:
        effectsound.soundHitPlay()
        haveDamage()