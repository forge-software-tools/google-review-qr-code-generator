# Google Review QR Code Generator (Python)

A simple Python script to generate **static, non-expiring QR codes** that link directly to the "Write a Review" page for any Google Business Profile.

## Live Demo
Don't want to run the code? Use the free web version here:
 **[Google Review QR Generator (Web Tool)](https://reviewreport.biz/tools/google-review-qr-code-generator)**

## Why use this?
Most "free" QR code generators create **dynamic links** (e.g., `qr.co/xyz`) that redirect to Google. The problem? They often expire after 14 days unless you pay a subscription.

This script uses the **Google Places API** to get your Place ID (`ChIJ...`) and constructs a direct, permanent Google Maps link:
`https://search.google.com/local/writereview?placeid=YOUR_PLACE_ID`

## Installation

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install requests qrcode[pil]
Get a Google Places API Key (from Google Cloud Console).

## Usage
python qr_generator.py
It will ask for your Business Name, find the Place ID, and save a review-qr.png file.

## Powered By
This tool is a simplified version of the engine behind ReviewReport – an AI reputation management dashboard for restaurants.
