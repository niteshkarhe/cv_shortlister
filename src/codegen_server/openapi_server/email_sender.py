import smtplib
from email.message import EmailMessage

def send_email_gmail(subject, message, destination):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #This is where you would replace your password with the app password
    server.login('service.punebot@gmail.com', 'nrdnfjcpruhgysni')

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message, subtype='html')
    msg['Subject'] = subject
    msg['From'] = 'me123@gmail.com'
    msg['To'] = destination
    server.send_message(msg)

body='''
<!DOCTYPE html>
<html>
    <!-- Complete Email template -->

<body style="background-color:grey"> 
	<table align="center" border="0" cellpadding="0" cellspacing="0"
		width="550" bgcolor="white" style="border:2px solid black"> 
		<tbody> 
			<tr> 
				<td align="center"> 
					<table align="center" border="0" cellpadding="0"
						cellspacing="0" class="col-550" width="550"> 
						<tbody> 
							<tr> 
								<td align="center" style="background-color: blue;
										height: 50px;"> 

									<a href="#" style="text-decoration: none;"> 
										<p style="color:white; 
												font-weight:bold;"> 
									TSYS Global Payment
										</p> 
									</a> 
								</td> 
							</tr> 
						</tbody> 
					</table> 
				</td> 
			</tr> 
			
					<p class="data"
					style="text-align: justify-all; 
							align-items: center; 
							font-size: 10x; 
							padding-bottom: 12px;"> 
					<p style="color:black
												font-weight:bold;"> 
											Dear Candidate , 
										</p> 

We are pleased to inform you that your application for the [Position Title] at [Company Name] has been successful, and we would like to invite you for a job interview.
This interview will provide us with an opportunity to further discuss your skills, suitability for the role, and to learn more about your career aspirations.
</p>
<p>
Date: [Interview Date] 
</p>
Time: [Interview Time] 
<p>
Location: [Interview Location/Video Call Details]
					</p>  
				</td> 
			</tr> 
			<tr style="border: none; 
			background-color: blue; 
			height: 40px; 
			color:white; 
			padding-bottom: 20px; 
			text-align: center;"> 
				
<td height="40px" align="center"> 
	<p style="color:white; 
	line-height: 1.5em;font-weight:bold;"> 
	TSYS Global Payment
	</p> 
	<a href="#"
	style="border:none; 
		text-decoration: none; 
		padding: 5px;"> 
			
	<img height="30"
	src= 
"https://extraaedgeresources.blob.core.windows.net/demo/salesdemo/EmailAttachments/icon-twitter_20190610074030.png"
	width="30" /> 
	</a> 
	
	<a href="#"
	style="border:none; 
	text-decoration: none; 
	padding: 5px;"> 
	
	<img height="30"
	src= 
"https://extraaedgeresources.blob.core.windows.net/demo/salesdemo/EmailAttachments/icon-linkedin_20190610074015.png"
width="30" /> 
	</a> 
	
	<a href="#"
	style="border:none; 
	text-decoration: none; 
	padding: 5px;"> 
	
	<img height="20"
	src= 
"https://extraaedgeresources.blob.core.windows.net/demo/salesdemo/EmailAttachments/facebook-letter-logo_20190610100050.png"
		width="24"
		style="position: relative; 
			padding-bottom: 5px;" /> 
	</a> 
</td> 
</tr> 
<tr> 
<td style="font-family:'Open Sans', Arial, sans-serif; 
		font-size:11px; line-height:18px; 
		color:#999999;" 
	valign="top"
	align="center"> 
<a href="#"
target="_blank"
style="color:#999999; 
		text-decoration:underline;">PRIVACY STATEMENT</a> 
		| <a href="#" target="_blank"
		style="color:#999999; text-decoration:underline;">TERMS OF SERVICE</a> 
		| <a href="#"
		target="_blank"
		style="color:blue; text-decoration:underline;">RETURNS</a><br> 
				© 2023 TSYS GlobalPaymentl Rights Reserved.<br> 
								<a href="#"
				target="_blank"
				style="text-decoration:none; 
						color:#999999;">unsubscribe</a> 
			</td> 
			</tr> 
			</tbody></table></td> 
		</tr> 
		<tr> 
		<td class="em_hide"
		style="line-height:1px; 
				min-width:700px; 
				background-color:blue;
			<img alt=""
			src="images/spacer.gif"
			style="max-height:1px; 
			min-height:1px; 
			display:block; 
			width:700px; 
			min-width:700px;" 
			width="700"
			border="0"
			height="1"> 
			</td> 
		</tr> 
		</tbody> 
	</table> 
</body> 

</html>
'''

send_email_gmail('Your resume is shortlisted', body, 'nitesh.karhe@gmail.com')