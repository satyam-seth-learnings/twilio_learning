- [Record an inbound call](https://www.twilio.com/docs/voice/tutorials/how-to-record-phone-calls/python#record-an-inbound-call)

# How to run

- Create virtual envirement

  ```bash
  python -m venv .venv
  ```

- Activate virtual envirement

  ```bash
  source .venv/bin/activate
  ```

- Install requirements

  ```bash
  pip install -r requirements.txt
  ```

- Run `python answer_phone.py` file

  ```bash
  python python app.py
  ```

- [Setup ngrok](https://dashboard.ngrok.com/get-started/setup/linux)

- Run ngrok

  ```bash
  ngrok http 5000
  ```

- [Configure your webhook URL](https://www.twilio.com/docs/voice/quickstart/python#configure-your-webhook-url)

- [Get Call Recording](https://console.twilio.com/us1/monitor/logs/call-recordings)
