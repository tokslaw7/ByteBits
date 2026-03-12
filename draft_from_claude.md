# ByteBites UML Class Diagram

```
┌─────────────────────────────┐
│           Customer          │
├─────────────────────────────┤
│ - username: String          │
│ - purchase_history: List    │
├─────────────────────────────┤
│ + getHistory(): List        │
│ + verify(): Boolean         │
└─────────────┬───────────────┘
              │ 1
              │ has many
              │ *
┌─────────────▼───────────────┐
│          Transaction        │
├─────────────────────────────┤
│ - transaction_id: String    │
│ - selected_items: List      │
│ - total_price: Float        │
├─────────────────────────────┤
│ + computeTotal(): Float     │
│ + getReceipt(): String      │
└─────────────┬───────────────┘
              │ *
              │ contains
              │ 1..*
┌─────────────▼───────────────┐
│           MenuItem          │
├─────────────────────────────┤
│ - name: String              │
│ - price: Float              │
│ - category: String          │
│ - popularity_rating: Float  │
└─────────────────────────────┘
              ▲
              │ managed by
              │
┌─────────────┴───────────────┐
│             Menu            │
├─────────────────────────────┤
│ - items: List<MenuItem>     │
├─────────────────────────────┤
│ + filterByCategory(): List  │
│ + getAllItems(): List        │
└─────────────────────────────┘

Enumerations:
┌──────────────┐
│  OrderType   │
├──────────────┤
│ BREAKFAST    │
│ LUNCH        │
└──────────────┘

┌──────────────┐
│   Category   │
├──────────────┤
│ FOOD         │
│ DRINKS       │
│ DESSERTS     │
└──────────────┘
```

## Key Relationships
- `Customer` 1 → * `Transaction` (one customer has many transactions)
- `Transaction` * → 1..* `MenuItem` (a transaction holds one or more items)
- `Menu` aggregates `MenuItem` objects and supports filtering by `Category`

The `transaction_id` links `Transaction` back to `Customer.purchase_history`, serving as the audit trail for past purchases.
