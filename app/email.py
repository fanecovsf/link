import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import List
from .exceptions import EmailException, AttachmentException, PathException
import os


class Email:
    """
    Classe para criar uma instância de email, usado para enviar avisos, alertas, etc...
    """

    def __init__(
            self,
            smtp_server: str,
            smtp_port: int,
            smtp_username: str,
            smtp_password: str,
            receivers: List[str],
            subject: str,
            email_body: str,
            attachments: List[str] = None,
            cco: List[str] = None,
            html_body: bool = False,
    ) -> None:
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.receivers = receivers
        self.cco = cco
        self.subject = subject
        self.email_body = email_body
        self.attachments = attachments
        self.html_body = html_body
    
    
    @property
    def _msg(self) -> MIMEMultipart:
        """
        Instanciando e configurando classes MIME
        """
        msg = MIMEMultipart()
        msg['From'] = self.smtp_username

        if self.cco:
            # Configurando a cópia oculta
            msg['Bcc'] = ', '.join(self.cco)

        if self.attachments:
            # Configurando os anexos (se existir)
            for file in self.attachments:
                if not os.path.exists(file):
                    raise PathException(f'Invalid path: {file}')

                try:
                    _attachment = open(file, 'rb')
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(_attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename= {file}')
                    msg.attach(part)
                except Exception as e:
                    raise AttachmentException(e)

        msg['Subject'] = self.subject

        body_map = {
            True: 'html',
            False: 'plain',
        }

        msg.attach(MIMEText(self.email_body, body_map[self.html_body]))

        return msg

    def send(self) -> None:
        """
        Método que irá fazer o envio do email baseado na instância da classe
        """
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)

            server.sendmail(self.smtp_username, self.receivers, self._msg.as_string())
        except Exception as e:
            raise EmailException(e)
        finally:
            server.quit()

