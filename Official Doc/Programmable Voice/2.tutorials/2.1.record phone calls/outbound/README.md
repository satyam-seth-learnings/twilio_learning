- [Make and record an outbound call](https://www.twilio.com/docs/voice/tutorials/how-to-record-phone-calls/python#make-and-record-an-outbound-call)

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

- Update env variables in `run.sh` file

- Add `execute` permission for run.sh file

  ```bash
  chmod +x ./run.sh
  ```

- Run `app.py` file

  ```bash
  ./run.sh
  ```

- [Get Call Recording](https://console.twilio.com/us1/monitor/logs/call-recordings)

# Tips for production

- Use [.env](https://github.com/theskumar/python-dotenv) file for env variables
