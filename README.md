# WA Perception Challenge
## Libraries Used
- OpenCV
- NumPy


# Methodology & Attempts
## Attempt 1
- At first, I just wanted to be able to get OpenCV be able to identify the cones in the image. For this I had CV identify any red that looked like the cones and have lines run through any detected cones. However, the issue that came up with this is that any red detected was identifying as a point for lines to run through. There was also no structure to the lines at all and they were all over the place(See wrong_answer.png)

## Attempt 2
- I realized that I would have to take a different approach in order to be able to have lines accurate run through the right side of the cones. I decided that the best way to do this would be to divide the image into two, and then run lines through the two halves because then there would just be one line of cones to run through. Additionally, I also determined the centers of the cones because previously, the lines were running to edges of the identified cones. By getting the centers of the cones, I was able to find the most accurate points to run the lines through. I also wanted to only create a singular line, so I would find the average slope and also find the intercept and run the line through the halves only one time. (See answer.png)