import sys
import re

class NyanTranspiler:
    def __init__(self):
        # 냥스크립트 -> 파이썬 키워드 매핑
        self.map = {
            r'기지개': 'if __name__ == "__main__"', 
            r'식빵굽기': 'pass',                   
            r'박스': '',                           # 변수 선언 삭제
            r'야옹': 'print',                      
            r'쫑긋': 'input',                      
            r'꾹꾹이': 'while',                    
            r'간식주면': 'if',                     
            r'아니면': 'else',                     
            r'하악질': 'raise Exception',          
            r'잡았다': 'True',                     
            r'놓쳤다': 'False',                    
            r'그루밍': '#',                        
        }

    def transpile(self, code):
        lines = code.split('\n')
        py_lines = []
        indent_level = 0
        
        for line in lines:
            # 1차 정리: 앞뒤 공백 제거
            line = line.strip()
            if not line: continue

            # 1. 닫는 중괄호 '}' 처리
            if '}' in line:
                indent_level = max(0, indent_level - 1)
                line = line.replace('}', '')
                
            # 2. 키워드 치환
            for nyan_key, py_key in self.map.items():
                line = line.replace(nyan_key, py_key)
                
            # [✨ 추가할 코드] C스타일 주석(//)을 파이썬 주석(#)으로 변환
            line = line.replace('//', '#')                
            
            # [✅ 중요 수정] 치환 후 '박스 ' 처럼 키워드 뒤에 남은 공백을 다시 한 번 제거!
            line = line.strip()
            if not line: continue

            # 3. 여는 중괄호 '{' 처리
            if '{' in line:
                line = line.replace('{', ':')
                increment_indent = True
            else:
                increment_indent = False

            # 4. 들여쓰기 적용
            indent_str = '    ' * indent_level
            py_lines.append(f"{indent_str}{line}")

            if increment_indent:
                indent_level += 1

        return '\n'.join(py_lines)

    def execute(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source_code = f.read()
            
            py_code = self.transpile(source_code)
            
            # 디버깅: 깔끔해진 코드 확인
            # print("=== 📜 변환된 파이썬 코드 ===")
            # print(py_code)
            # print("===========================\n")

            exec(py_code, globals())
            
        except IndentationError as e:
            print(f"😿 들여쓰기 오류다냥! 줄을 맞춰라냥: {e}")
        except Exception as e:
            print(f"😿 실행 중 하악질 발생: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python nyan.py [파일이름.nyan]")
    else:
        interpreter = NyanTranspiler()
        interpreter.execute(sys.argv[1])