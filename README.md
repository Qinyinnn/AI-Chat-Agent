# AI Chat Assistant with Advanced Calculator

An intelligent chat agent built with LangChain that combines conversational AI with advanced mathematical capabilities.

## Features

- **Advanced Calculator:**
  - Symbolic mathematics operations
  - Calculus operations (derivatives, integrals)
  - Expression simplification
  - Basic arithmetic
  
- **Time Services:**
  - Get current time in any timezone
  
- **URL Management:**
  - URL shortening capabilities
  
- **Conversational Interface:**
  - Natural language interaction
  - Friendly AI assistant personality (Youri)

## Setup

1. Clone the repository
```bash
git clone <your-repository-url>
cd ai-chat-agent
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key
```bash
OPENAI_API_KEY=your_api_key_here
```

4. Run the application
```bash
python main.py
```

## Usage Examples

```
You: Calculate the derivative of x^2
Youri: The derivative of x^2 with respect to x is 2x

You: What time is it in Tokyo?
Youri: Current time in Asia/Tokyo is 2023-12-25 12:00:00

You: Shorten this URL: https://example.com
Youri: Here's your shortened URL: https://tinyurl.com/...
```

## Dependencies

- LangChain
- OpenAI
- SymPy
- PyTZ
- PyShorteners

## License

MIT License