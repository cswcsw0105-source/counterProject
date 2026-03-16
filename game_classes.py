# game_classes.py

from abc import ABC, abstractmethod

# 모든 직업의 공통적인 틀이 되는 추상 클래스
class GameCharacter(ABC):
    def __init__(self, name, job, health, energy_name):
        self.name = name
        self.job = job
        self.health = health
        self.current_health = health
        self.energy_name = energy_name
        self.energy = 100 # 기본 에너지

    @abstractmethod
    def primary_attack(self, target):
        """평타 스킬"""
        pass

    @abstractmethod
    def utility_skill(self):
        """이동기 또는 유틸 스킬"""
        pass

    @abstractmethod
    def defensive_skill(self):
        """방어 또는 회피 스킬"""
        pass

    def take_damage(self, damage):
        self.current_health -= damage
        print(f"[{self.name}]님이 {damage} 데미지를 입었습니다. (남은 체력: {self.current_health})")

# 1. 워리어 클래스
class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name, "워리어", health=200, energy_name="분노")

    def primary_attack(self, target):
        damage = 25
        print(f"[{self.name}] 근접공격! {target.name}에게 도끼를 휘둘러 {damage} 피해를 입힙니다.")
        target.take_damage(damage)

    def utility_skill(self):
        print(f"[{self.name}] 돌진! 저돌적으로 적에게 접근합니다.")
        # 추가적인 이동 로직 (탑뷰 좌표 이동 등)

    def defensive_skill(self):
        print(f"[{self.name}] 방어! 단단히 자세를 잡고 방어력을 극대화합니다. (패링 없음)")
        # 데미지 감소 버프 등

# 2. 헌터 클래스
class Hunter(GameCharacter):
    def __init__(self, name):
        super().__init__(name, "헌터", health=150, energy_name="집중")

    def primary_attack(self, target):
        damage = 18
        print(f"[{self.name}] 중거리 공격! {target.name}에게 화살을 쏘아 {damage} 피해를 입힙니다.")
        target.take_damage(damage)

    def utility_skill(self):
        print(f"[{self.name}] 은신! 그림자 속으로 몸을 숨깁니다.")
        # 일시적 투명 상태 로직

    def defensive_skill(self):
        print(f"[{self.name}] 패링 및 가드! 상대의 공격 타이밍을 노려 패링하거나 막습니다.")
        # 반격 로직, 혹은 무력화(CC) 로직

# 3. 마법사 클래스
class Wizard(GameCharacter):
    def __init__(self, name):
        super().__init__(name, "마법사", health=100, energy_name="마나")

    def primary_attack(self, target):
        damage = 30
        print(f"[{self.name}] 원거리 공격! {target.name}에게 마법 화살을 날려 {damage} 피해를 입힙니다.")
        target.take_damage(damage)

    def utility_skill(self):
        print(f"[{self.name}] 순간이동! 지정된 위치로 즉시 이동합니다.")
        # 좌표 이동 로직

    def defensive_skill(self):
        print(f"[{self.name}] 방어막! 자신을 보호하는 마력 방어막을 생성합니다.")
        # 데미지 흡수막 로직

# --- 테스트 실행 (실제 게임 로직은 아님) ---
if __name__ == "__main__":
    warrior_p1 = Warrior("전사형")
    wizard_p2 = Wizard("마법형")
    hunter_p3 = Hunter("사냥꾼형")

    # 가상 대전 상황
    print(f"=== 대전 시작: {warrior_p1.name} vs {wizard_p2.name} ===\n")
    
    warrior_p1.utility_skill() # 돌진
    warrior_p1.primary_attack(wizard_p2) # 근접공격

    wizard_p2.defensive_skill() # 방어막
    wizard_p2.primary_attack(warrior_p1) # 원거리공격
    wizard_p2.utility_skill() # 순간이동 (거리 벌리기)

    print("\n")
    hunter_p3.defensive_skill() # 헌터의 패링/가드
