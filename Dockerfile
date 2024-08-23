# Use a Windows base image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Switch to PowerShell
SHELL ["powershell", "-Command"]

# Install Python
RUN Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe -OutFile python-installer.exe; \
    Start-Process python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -NoNewWindow -Wait; \
    Remove-Item -Force python-installer.exe

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your Python script into the container
COPY gui.pyw C:/app/gui.py

# Set the working directory
WORKDIR C:/app

# Build the .exe file
RUN pyinstaller --onefile gui.py

# Define a command to keep the container alive for manual inspection (optional)
CMD ["powershell"]
