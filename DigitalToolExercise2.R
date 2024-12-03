

library(ggplot2)

trade_data <- read.csv("~/Desktop/historical_trade_data.csv")

head(trade_data)
str(trade_data)

high_exports <- trade_data[trade_data$Exports > 200000, ]

trade_data$Trade_Balance <- trade_data$Exports - trade_data$Imports

trade_plot <- ggplot(trade_data, aes(x = Year, y = Trade_Balance)) +
  geom_line(color = "blue") +
  labs(title = "Trade Balance Over Time", x = "Year", y = "Trade Balance")

print(trade_plot)

ggsave("~/Desktop/trade_balance_plot.png", plot = trade_plot)


