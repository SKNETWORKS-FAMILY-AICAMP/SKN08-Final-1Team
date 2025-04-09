import 'package:jobstick/kakao_authentication/domain/usecase/request_user_token_usecase.dart';
import '../../infrasturcture/repository/kakao_auth_repository.dart';

class RequestUserTokenUseCaseImpl implements RequestUserTokenUseCase {
  final KakaoAuthRepository repository;

  RequestUserTokenUseCaseImpl(this.repository);

  @override
  Future<String> execute(
      String accessToken, int userId, String email, String nickname, String gender, String ageRange, String birthyear) async {
    try {
      // Django 서버로 요청하여 User Token 반환
      final userToken =
      await repository.requestUserToken(accessToken, userId, email, nickname, gender, ageRange, birthyear);
      print("User token obtained: $userToken");
      return userToken;
    } catch (error) {
      print("Error while requesting user token: $error");
      throw Exception('Failed to request user token: $error');
    }
  }
}