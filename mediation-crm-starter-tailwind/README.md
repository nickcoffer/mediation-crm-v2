# MEDIATION CRM - Installation Guide

## What you need (ONE-TIME SETUP)

Before you can use the CRM, you need to install two free programs:

### 1. Python (10 minutes)
- **Windows:** Go to https://python.org/downloads → Download → Run installer
  - ⚠️ IMPORTANT: Tick the box "Add Python to PATH" before clicking Install
- **Mac:** Go to https://python.org/downloads → Download → Run installer

### 2. Node.js (5 minutes)
- Go to https://nodejs.org
- Download the LTS version (left button)
- Run the installer

---

## Setting up the CRM (ONE-TIME, 5-10 minutes)

Once Python and Node.js are installed:

### Windows:
1. Double-click `SETUP.bat`
2. Wait while it installs (2-3 minutes) - text will scroll by, this is normal!
3. When it says "Setup complete", you're done!

### Mac:
1. Right-click `SETUP.command` → Open
2. If you get a security warning, click "Open anyway"
3. Wait while it installs (2-3 minutes)
4. When it says "Setup complete", you're done!

**No login needed!** The CRM opens directly to your dashboard.

---

## Using the CRM (EVERY DAY - EASY!)

### Windows:
1. Double-click `START-CRM.bat`
2. Two black windows will open - DON'T CLOSE THEM
3. Your browser opens automatically showing the CRM
4. When finished, close the two black windows

### Mac:
1. Right-click `START-CRM.command` → Open
2. Two terminal windows open - DON'T CLOSE THEM
3. Your browser opens automatically showing the CRM
4. When finished, close the two terminal windows

---

## Troubleshooting

**"Python not found" or "Node not found"**
- You need to install Python and Node.js first (see above)
- Windows users: Make sure you ticked "Add Python to PATH"

**"Port already in use"**
- Something else is using port 3000 or 8000
- Close other programs and try again

**Still stuck?**
- Call/text Nick - he'll help you out!

---

## Your Data

All your data is stored on YOUR computer in the `backend/db.sqlite3` file.

**To backup:** Just copy that file somewhere safe (USB drive, cloud storage, etc.)

**To restore:** Replace the file with your backup

---

Enjoy your CRM! 🎉
