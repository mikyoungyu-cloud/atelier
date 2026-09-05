import asyncio
import edge_tts
import os

async def text_to_speech(text, filename="output.mp3", voice="en-US-JennyNeural"):
    """
    Edge TTS를 사용하여 텍스트를 훨씬 더 자연스러운 음성(MP3)으로 변환합니다.
    """
    try:
        # Communicate 객체 생성
        communicate = edge_tts.Communicate(text, voice)
        
        # 파일로 저장
        await communicate.save(filename)
        print(f"성공적으로 '{filename}' 파일이 생성되었습니다.")
        
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    # 변환하고 싶은 스크립트를 여기에 입력하세요.
    script_text = """I want to go to Paris, France.
First, I am going to go to the Eiffel Tower.
I'm going to walk around the Eiffel Tower and take a cruise, too.
Second, I am going to visit the Louvre Museum.
I'm going to see some artwork.
Lastly, I'm going to go to the Arc de Triomphe.
I'm going shopping.
I will eat some bread.
I'm going to buy and eat things like macarons and baguettes."""
    
    # 변환 실행 (원하는 파일명으로 변경 가능)
    # asyncio.run을 사용하여 비동기 함수를 실행합니다.
    asyncio.run(text_to_speech(script_text, filename="my_script.mp3", voice="en-US-JennyNeural"))
