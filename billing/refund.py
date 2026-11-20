# Billing refund service
def process_instant_refund(customer_id: str, amount_cents: int) -> bool:
    # Missing 2FA confirmation and BigQuery audit emission
    return gateway.refund(customer_id, amount_cents)
