from sqlalchemy import exc
from sqlalchemy.orm import Session
from api.models import Transaction


class TransactionService:
    def __init__(self, db: Session):
        self.db = db

    def transaction_sync(self, data_body):
        dict_data = data_body.dict()

        data = {
            'transaction_id': dict_data['transactionid'],
            'transaction_time': dict_data['transactiontime'],
            'reference_number': dict_data['referencenumber'],
            'amount': dict_data['amount'],
            'content': dict_data['content'],
            'bank_account': dict_data['bankaccount'],
            'trans_type': dict_data.get('transType'),
            'value_date': dict_data.get('valueDate'),
            'va': dict_data.get('va'),
            'reciprocal_account': dict_data.get('reciprocalAccount'),
            'reciprocal_bank_code': dict_data.get('reciprocalBankCode')
        }

        new_transaction = Transaction(**data)
        try:
            self.db.add(new_transaction)
        except exc.DatabaseError as e:
            raise e

        self.db.commit()
        self.db.refresh(new_transaction)
        return new_transaction
