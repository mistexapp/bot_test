FROM python:3.8

ENV TG_TOKEN=${{ secrets.TG_TOKEN }}
ENV TG_ADMIN=${{ secrets.TG_ADMIN }}
#'360873310'
#'5054086490:AAHHt6-CCOCfV2O_QLQqlrRG9-qwBGsde2Y'

COPY * .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "bot.py"]
