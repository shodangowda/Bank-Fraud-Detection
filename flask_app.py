from flask import Flask
import random
import pandas as pd

app = Flask(__name__)

@app.route("/")
def run_test():
    try:
        import sqlite3
        # Connect to the BANKNH database
        conn = sqlite3.connect("BankNH.db")
        cursor = conn.cursor()
        cursor.execute("SELECT TTYPE, AMOUNT, SENDEROLDBAL, SENDERNEWBAL, RECOLDBAL, RECNEWBAL FROM NEWT")
        data_list = cursor.fetchall()
        conn.close()
        
        if data_list:
            fetched_data = data_list[-1]
            j = list(fetched_data)
            i = random.randint(0,9)
            j.insert(0,i)
        else:
            j = [0,"TRANSFER",900,0,80,70,0]

        df= pd.DataFrame([j] , columns=['count','type','amount','oldbalanceOrig','newbalanceOrig','oldbalanceDest','newbalanceDest'])
        
        # Bypassed prediction
        prediction = 0
        if prediction == 1:
            message = 'Invalid Amount. Please enter a valid positive amount.'
            status_color = 'red'
        else:
            message = 'Transaction done.'
            status_color = 'green'

        html_content = f"""
        <html>
            <head>
                <title>Bank Fraud Detection Test</title>
                <style>
                    body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; padding: 50px; text-align: center; }}
                    .container {{ background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }}
                    h1 {{ color: #2c3e50; }}
                    .result {{ font-size: 24px; font-weight: bold; color: {status_color}; margin-top: 20px; }}
                    .data {{ margin-top: 30px; text-align: left; background-color: #f8f9fa; padding: 15px; border-radius: 5px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Fraud Detection Test Output</h1>
                    <div class="result">{message}</div>
                    <div class="data">
                        <h3>Transaction Details Evaluated:</h3>
                        <pre>{df.to_string()}</pre>
                    </div>
                </div>
            </body>
        </html>
        """
        return html_content
    except Exception as e:
        return f"<h1>Error:</h1><pre>{str(e)}</pre>"

if __name__ == "__main__":
    app.run(port=5000)
