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
<img width="590" alt="Screenshot 2023-04-16 at 23 43 46" src="https://user-images.githubusercontent.com/104798477/232347153-236d92b4-8fda-43c1-b74e-3286bc58b49d.png">

- In this thread you upload the images of the receipts
- You must also write the names for who the money is owed to/paid for the receipt's cost
<img width="505" alt="Screenshot 2023-04-17 at 00 02 31" src="https://user-images.githubusercontent.com/104798477/232347939-72828be1-4385-4fdf-ae39-57bf9db378df.png">

- Upon hitting enter, the bot will look at each image one by one
- You can send more images after the initial scan to be added to the CSV file
<img width="336" alt="Screenshot 2023-04-17 at 00 05 28" src="https://user-images.githubusercontent.com/104798477/232348089-fe71fe85-0302-43bf-b48c-3521a0a906ff.png">

- When finished the user must run the command `$done` to close the thread
- This will also return the CSV file in the origin channel where the `$scan` command was run
<img width="240" alt="Screenshot 2023-04-17 at 01 05 34" src="https://user-images.githubusercontent.com/104798477/232351278-9a79e2cb-ad43-4f08-9870-ca3bdc95369e.png">
<img width="246" alt="Screenshot 2023-04-17 at 01 05 55" src="https://user-images.githubusercontent.com/104798477/232351293-2708d6b5-f001-4b4b-8232-d0176aba22cc.png">

- These CSV files can be opened in softwares such as Excel or Google sheet to make any changes or fix any errors

## Important
- Please be advised that this bot is not 100% accurate with every image scan
- For the most accurate results, please ensure the image of the receipt has good lighting and the total price is clearly visible
- If the total cost cannot be found, 0.0 will be used as the placeholder value (this can be changed in the CSV file)
- You will need to use your own Discord API key if you are to use this in your own server
