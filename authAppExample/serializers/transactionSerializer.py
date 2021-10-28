from authAppExample.models.account     import Account
from authAppExample.models.user        import User
from authAppExample.models.transaction import Transaction
from rest_framework                    import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Transaction
        fields = ["origin_account", "destiny_account", "amount", "register_date", "note"]

    def to_representation(self, obj):
        transaction     = Transaction.objects.get(id=obj.id)
        origin_account  = Account.objects.get(id=transaction.origin_account_id)
        destiny_account = Account.objects.get(id=transaction.destiny_account_id)
        destiny_user    = User.objects.get(id=destiny_account.user_id)
        return {
            'id'           : transaction.id,
            'amount'       : transaction.amount,
            'register_date': transaction.register_date,
            'note':          transaction.note,
            'origin_account': {
                'id'     :origin_account.id,
                'balance':origin_account.balance
            },
            'destiny_account':{
                'id'   : destiny_account.id,
                'user' : destiny_user.name
            }
            
        }
