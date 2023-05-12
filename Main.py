
import pygame  
import notas
pygame.init() 
Pantalla = pygame.display.set_mode((800, 500))
running = True


pianoimg = pygame.image.load('Piano.png')
pianoimg = pygame.transform.scale(pianoimg,(800,500)) #escala el piano para ajustarlo a la pantalla
Dedoimg = pygame.image.load('Dedo.png')
Dedoimg = pygame.transform.scale(Dedoimg,(100,100)) #escala la mano

frames = pygame.time.Clock() 
posy=400 #
posx=-100 #posicion de la mano
#pygame.key.set_repeat()


while running:
    # si se apreta la cruz se sale del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # toco y suena al presionar
        if event.type == pygame.KEYDOWN:
          
            if event.key == pygame.K_e:
                
                posx=10
                notas.reproducirDO(1)
                
                
            elif event.key == pygame.K_r:
               
                posx=110
                notas.reproducirre(1)
               
            elif event.key == pygame.K_t:
                
                posx=210
                notas.reproducirmi(1)
                
            elif event.key == pygame.K_y:                
                posx=310
                notas.reproducirfa(1)
                
            elif event.key == pygame.K_u:               
                posx=410
                notas.reproducirsol(1)
                
            elif event.key == pygame.K_i:              
                posx=510
                notas.reproducirla(1)
                
            elif event.key == pygame.K_o:             
                posx=610
                notas.reproducirsi(1)
                
            elif event.key == pygame.K_p:            
                posx=710
                notas.reproducirdo2(1)
        
     #deja de sonar la nota
        if event.type == pygame.KEYUP:
          
            if event.key == pygame.K_e:
                
                posx=10
                notas.reproducirDO(0)
                
                
            elif event.key == pygame.K_r:
               
                posx=110
                notas.reproducirre(0)
               
            elif event.key == pygame.K_t:
                
                posx=210
                notas.reproducirmi(0)
                
            elif event.key == pygame.K_y:                
                posx=310
                notas.reproducirfa(0)
                
            elif event.key == pygame.K_u:               
                posx=410
                notas.reproducirsol(0)
                
            elif event.key == pygame.K_i:              
                posx=510
                notas.reproducirla(0)
                
            elif event.key == pygame.K_o:             
                posx=610
                notas.reproducirsi(0)
                
            elif event.key == pygame.K_p:            
                posx=710
                notas.reproducirdo2(0)             
       
            
            
                    
   
    
    # fill the screen with a color to wipe away anything from last frame
    Pantalla.fill("brown")
    # RENDER YOUR GAME HERE
   
    Pantalla.blit(pianoimg,(0,0)) #coloca la imagen del piano
    Pantalla.blit(Dedoimg,(posx,posy))  #Dibuja la mano que presiona las teclas
    

        
   
    
    


    # actualizar pantalla
    pygame.display.flip()
    pygame.display.update()

    frames.tick(60)  # limits FPS to 60

pygame.quit()
