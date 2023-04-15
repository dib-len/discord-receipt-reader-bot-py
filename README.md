# Discord Receipt Reader Bot
A Discord bot that allows users to send pictures of receipts, along with the names of who purchased the receipt, and then creates a CSV file containing the total cost of the receipt and who paid the fee. <br/> <br/>
The idea came from when the treasurer at the RHUL Computer Science society had to manually add the total costs (along with who the money was owed to) into Google Sheets, for several receipt images in our Discord server.

## Packages Used
- os
- dotenv
- discord
- discord.ext
- pytesseract
- cv2 (OpenCV)
- numpy
- re
- pandas

## Key Features
- Running the command `$receipt` creates a new thread which is used to upload the images of receipts
- Upload the images, the command `$scan` along with the names (in the same message containing the image) for it to create a CSV file

## Example
- To begin, the command `$receipt` is run, creating a new thread
<img width="611" alt="Screenshot 2023-04-15 at 01 13 24" src="https://user-images.githubusercontent.com/104798477/232173090-e094f0fd-ecd0-4dea-ad34-fca90b42fe74.png">

- In this thread you upload the images of the receipt
- You must also write the names for who the money is owed to/paid for the receipt's cost
<img width="553" alt="Screenshot 2023-04-15 at 01 16 40" src="https://user-images.githubusercontent.com/104798477/232173198-39ac1b43-a019-4d60-a511-a06268288325.png">

- Upon hitting enter, the bot will look at each image one by one
- It then returns a CSV file containing this information
<img width="310" alt="Screenshot 2023-04-15 at 01 19 21" src="https://user-images.githubusercontent.com/104798477/232173554-02aa6900-56c7-4ff4-9e17-520653752a4c.png">
<img width="270" alt="Screenshot 2023-04-15 at 01 19 42" src="https://user-images.githubusercontent.com/104798477/232173571-13227d0b-359c-43d2-a64e-0a52237ae350.png">

- This CSV file can be opened in softwares such as Excel or Google sheet to make any fixes or changes

## Important
- Please be advised that this bot is not perfect by any means
- It may not detect the total costs, however, it has several error handlers to deal with this
- You will need to use your own Discord API key if you are to use this in your own server
