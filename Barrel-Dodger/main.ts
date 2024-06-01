controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
	
})
tiles.setTilemap(tilemap`level5`)
let mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . 5 . 5 . . . . . . . 
    . . . . . f 5 5 5 f . . . . . . 
    . . . . f 6 5 5 2 6 f . . . . . 
    . . . f 6 6 1 6 6 6 6 f . . . . 
    . . . f 6 1 6 6 6 6 6 f . . . . 
    . . . f 1 6 6 6 d f d f . . . . 
    . . f f 6 6 6 6 d f d f . . . . 
    . f 6 f 6 6 6 d d 3 d f . . . . 
    . . f f 6 f f d d d f . . . . . 
    . f 6 6 f f 3 3 f f . . . . . . 
    . . f f f d d 3 3 5 f . . . . . 
    . . . f d d f 3 3 3 f . . . . . 
    . . . . f f f 5 3 f . . . . . . 
    . . . . . f 3 3 3 3 f . . . . . 
    . . . . . f f f f f . . . . . . 
    `, SpriteKind.Player)
tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 5))
