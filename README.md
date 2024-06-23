# PropertySearchBotUsingCrewAiBot
Usng crewai powered bot to search for properties.

# Startup 
0. Create a virtual environment `py -m venv <name of environment>`
1. Activate virtual environment `.\<name of environment>\Scripts\activate`
2. Install initial dependency `py -m pip install -r requirements.txt`
3. Down load and install ollama from <a href="https://ollama.com/">Ollama</a>
4. Pull and run model. `ollama pull 'mistral:latest'` or model of choice and will need to change llm = Ollama(model="mistral:latest") in crewai_bot.py to model downloaded.
5. Update the `SERPER_API_KEY` value with an API key from <a href="https://serper.dev/api-key">Serper</a></p>
6. Run the flow using `python crewai_bot.py`
