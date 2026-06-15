// ─── Navigation ──────────────────────────────────────────────
export const navItems = [
  { label: 'Product', href: '#product' },
  { label: 'How It Works', href: '#how-it-works' },
  { label: 'Developers', href: '#developers' },
  { label: 'Company', href: '#company' },
];

// ─── Feature Cards ───────────────────────────────────────────
export interface FeatureCard {
  number: string;
  title: string;
  description: string;
  accent: 'ivory' | 'blue';
}

export const featureCards: FeatureCard[] = [
  {
    number: '01',
    title: 'AI Matching',
    description:
      'Real-time semantic matching powered by attendee behavior, profile signals, and event context.',
    accent: 'ivory',
  },
  {
    number: '02',
    title: 'Smart Introductions',
    description:
      'AI-crafted intros and contextual prompts that make every meeting more relevant.',
    accent: 'blue',
  },
  {
    number: '03',
    title: 'Network Intelligence',
    description:
      'Actionable insight into connection quality, room energy, and opportunity flow.',
    accent: 'ivory',
  },
];

// ─── Metrics ─────────────────────────────────────────────────
export interface Metric {
  value: string;
  label: string;
}

export const metrics: Metric[] = [
  { value: '48,200+', label: 'Attendees Processed' },
  { value: '12,800', label: 'Matches Made' },
  { value: '94%', label: 'Connection Rate' },
  { value: '3,400', label: 'Meetings Booked' },
  { value: '6.2 hrs', label: 'Avg. Time Saved' },
];

// ─── Trust Strip ─────────────────────────────────────────────
export const trustCompanies = ['Vercel', 'Linear', 'Figma', 'Ramp', 'Webflow'];

// ─── Match List ──────────────────────────────────────────────
export interface MatchEntry {
  name: string;
  role: string;
  company: string;
  score: number;
}

export const matchList: MatchEntry[] = [
  { name: 'Morgan Lee', role: 'Head of Growth', company: 'Linear', score: 96 },
  { name: 'Riley Chen', role: 'Product Designer', company: 'Figma', score: 92 },
  { name: 'Casey Jordan', role: 'Engineer', company: 'Vercel', score: 89 },
];

// ─── Live Event Stats ────────────────────────────────────────
export interface EventStat {
  value: string;
  label: string;
}

export const liveEvent = {
  name: 'Tech Week NYC',
  dates: 'May 15 – 17, 2025',
  venue: 'Pier 36',
  stats: [
    { value: '4,782', label: 'Attendees' },
    { value: '1,246', label: 'Connections' },
    { value: '328', label: 'Meetups' },
  ] as EventStat[],
};

// ─── Network Status ──────────────────────────────────────────
export const networkBars = [40, 55, 70, 85, 65, 78, 92, 60, 75, 88];

// ─── Site Meta ───────────────────────────────────────────────
export const siteMeta = {
  title: 'Tjenko — AI Networking Layer for Live Events',
  description:
    'Tjenko is the AI networking layer that understands live events and orchestrates meaningful connections in real time.',
};
