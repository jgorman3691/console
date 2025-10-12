from anthropic import Anthropic

client = Anthropic()

message = client.messages.create(
   model = "claude-sonnet-4-5",
   max_tokens = 1000,
   messages = [
      {
         "role": "user",
         "content": "What should I search for to find the most desired talents and abilities for an engineer looking to work as a quant in finance?"
      }
   ]
)
print(message.content)