import { atom } from "nanostores";

export const active = atom(true);
export const temperatures = atom([
	{
		temperature_limit: 25,
		visible: false,
	},
]);
