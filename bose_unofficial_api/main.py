# Example usage
import asyncio
import logging
import os

from speaker import BoseSpeaker


async def main():
    logging.basicConfig(level=logging.INFO)

    ip_address = os.environ.get("BOSE_IP_ADDRESS")
    jwt_token = os.environ.get("BOSE_JWT_TOKEN")

    if not ip_address or not jwt_token:
        raise Exception(
            "Please set the BOSE_IP_ADDRESS and BOSE_JWT_TOKEN environment variables"
        )

    speaker = await BoseSpeaker.connect(
        ip_address=ip_address,
        jwt_token=jwt_token,
        log_messages=True,
    )

    # Example of sending a message and waiting for its response
    nowPlaying = await speaker.get_now_playing()
    print("Now playing: %s", nowPlaying)

    await speaker.connection.close()


if __name__ == "__main__":
    asyncio.run(main())