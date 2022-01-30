# AI Rock Paper Scissors Robot  

![rps-gif](Resource/rps-gif.gif)

#### Full video [Here](https://youtu.be/jDaEojt1Owg)

## Set up instructions
1. Clone the repo.

2. Install the dependencies
```sh
$ pip install -r requirements.txt
```

3. Gather Images for each gesture (rock, paper and scissors and None):
In this example, we gather 200 images for the "rock" gesture
```sh
$ python3 gather_images.py rock 200
```

Press - 'a' to start/pause
Press - 'q' to quit

4. Train the model
```sh
$ python3 train_model.py
```

5. Test the model on some images
```sh
$ python3 test_model.py <path_to_test_image>
```

6. Upload Sketch using Arduino IDE
```
rockpaperbot.ino
```
Connect the Arduino to PC.

7. Start the game with your Bot!
```sh
$ python3 play.py
```