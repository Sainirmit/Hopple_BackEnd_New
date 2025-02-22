# utils/async_utils.py
import asyncio
from utils.logger import log_debug, log_error

# A simple in-memory cache
mistral_cache = {}

async def async_call_mistral(prompt: str) -> str:
    """
    Asynchronously calls Mistral via Ollama with the given prompt.
    Uses an in-memory cache to avoid duplicate calls.
    """
    if prompt in mistral_cache:
        log_debug(f"Cache hit for prompt: {prompt}")
        return mistral_cache[prompt]
    
    try:
        proc = await asyncio.create_subprocess_exec(
            "ollama", "run", "mistral", prompt,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            log_error(f"Error calling Mistral: {stderr.decode().strip()}")
            return ""
        output = stdout.decode().strip()
        log_debug(f"Mistral output for prompt '{prompt}': {output}")
        mistral_cache[prompt] = output  # Cache the result
        return output
    except Exception as e:
        log_error(f"Exception in async_call_mistral: {e}")
        return ""