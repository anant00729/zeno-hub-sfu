import { env } from '$env/dynamic/public';
import { OpenAPI, ZenoService } from '$lib/zenoapi';
import { redirect } from '@sveltejs/kit';

export async function load({ cookies, url }) {
	const userCookie = cookies.get('loggedIn');
	if (!userCookie) {
		throw redirect(303, `/login?redirectTo=${url.pathname}`);
	}
	const cognitoUser = JSON.parse(userCookie);
	// If the user is not authenticated, redirect to the login page
	if (!cognitoUser.id || !cognitoUser.accessToken) {
		throw redirect(303, `/login?redirectTo=${url.pathname}`);
	}

	OpenAPI.BASE = env.PUBLIC_BACKEND_ENDPOINT + '/api';
	const user = await ZenoService.login(cognitoUser.email);
	const organizations = await ZenoService.getOrganizations(user);

	return {
		cognitoUser: cognitoUser,
		user: user,
		organizations: organizations
	};
}